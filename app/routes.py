from flask import Blueprint, render_template, request
import os

bp = Blueprint("main", __name__)


def send_whatsapp_notification(payload: dict) -> tuple[bool, str]:
    provider = (os.getenv("WA_PROVIDER") or "").lower()
    to_number = os.getenv("WHATSAPP_TO")

    text = (
        f"Nuevo contacto\n"
        f"Nombre: {payload.get('name')}\n"
        f"Email: {payload.get('email') or '-'}\n"
        f"Teléfono: {payload.get('phone') or '-'}\n"
        f"Mensaje: {payload.get('message')}"
    )

    try:
        if provider == "cloud":
            import requests  # carga perezosa
            token = os.getenv("WHATSAPP_CLOUD_TOKEN")
            phone_number_id = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
            if not (token and phone_number_id and to_number):
                return False, "Faltan variables para WhatsApp Cloud"
            url = f"https://graph.facebook.com/v18.0/{phone_number_id}/messages"
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            data = {
                "messaging_product": "whatsapp",
                "to": to_number.replace(" ", ""),
                "type": "text",
                "text": {"body": text},
            }
            resp = requests.post(url, headers=headers, json=data, timeout=15)
            ok = 200 <= resp.status_code < 300
            return ok, "WhatsApp Cloud enviado" if ok else f"Error Cloud: {resp.text}"

        if provider == "twilio":
            import requests  # carga perezosa
            from requests.auth import HTTPBasicAuth
            sid = os.getenv("TWILIO_ACCOUNT_SID")
            token = os.getenv("TWILIO_AUTH_TOKEN")
            wa_from = os.getenv("TWILIO_WHATSAPP_FROM")
            if not (sid and token and wa_from and to_number):
                return False, "Faltan variables para Twilio"
            url = f"https://api.twilio.com/2010-04-01/Accounts/{sid}/Messages.json"
            resp = requests.post(
                url,
                data={"From": wa_from, "To": to_number, "Body": text},
                auth=HTTPBasicAuth(sid, token),
                timeout=15,
            )
            ok = 200 <= resp.status_code < 300
            return ok, "Twilio enviado" if ok else f"Error Twilio: {resp.text}"

        return False, "Proveedor WA no configurado"
    except Exception as exc:  # pragma: no cover
        return False, f"Excepción WA: {exc}"


@bp.get("/")
def home():
    # Carloszerpav: landing principal
    return render_template("index.html")


@bp.get("/proyectos")
def projects():
    projects_list = [
        {
            "title": "Sistema de Ventas",
            "stack": ["Python", "Flask", "PostgreSQL", "Railway"],
            "desc": "Sistema integral de gestión de ventas con autenticación segura mediante Google OAuth. Plataforma eficiente para administrar transacciones, inventario y reportes en tiempo real.",
            "url": "http://ventas-sistema-production.up.railway.app/",
            "category": "Web App",
            "image": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&h=400&fit=crop",
        },
        {
            "title": "Malva Shop",
            "stack": ["Catalog", "Web Design", "Railway"],
            "desc": "Catálogo digital interactivo especializado en accesorios y maquillaje original. Plataforma diseñada para exhibir productos de manera elegante y profesional, con integración directa de contacto mediante WhatsApp e Instagram para facilitar la comunicación entre clientes y vendedora.",
            "url": "http://malva-production.up.railway.app/",
            "category": "Catalog Platform",
            "image": "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=800&h=400&fit=crop",
        },
        {
            "title": "App Trader",
            "stack": ["Frontend", "JavaScript", "Trading", "Real-time", "Railway"],
            "desc": "Aplicación web frontend para traders con herramientas avanzadas de análisis de mercado y visualización de datos en tiempo real. Proyecto desarrollado con tecnologías modernas del lado del cliente, enfocado en una interfaz intuitiva y responsive para gestión de portafolios y seguimiento de activos.",
            "url": "https://app-trader-production-4221.up.railway.app/",
            "category": "Frontend App",
            "image": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800&h=400&fit=crop",
        },
        {
            "title": "Kaspersky Endpoint Security",
            "stack": ["Cybersecurity", "Enterprise", "Deployment", "Security Center"],
            "desc": "Despliegue y configuración de soluciones de seguridad Kaspersky para protección integral de sistemas empresariales. Implementación de Kaspersky Endpoint Security y gestión centralizada mediante Kaspersky Security Center.",
            "url": "https://www.kaspersky.com/",
            "category": "Security & Infrastructure",
            "image": "https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=800&h=400&fit=crop",
            "is_external": True,
        },
    ]
    return render_template("projects.html", projects=projects_list)


@bp.get("/servicios")
def services():
    return render_template("services.html")


@bp.route("/contacto", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        message = request.form.get("message", "").strip()

        has_contact = bool(email or phone)
        is_valid = bool(name and message and has_contact)

        submitted = {"name": name, "email": email, "phone": phone, "message": message}

        if not is_valid:
            error = "Por favor completa nombre, mensaje y al menos email o teléfono."
            return render_template("contact.html", error=error, form=submitted), 400

        print("[Contacto]", submitted)
        wa_sent = False
        wa_info = None
        ok, info = send_whatsapp_notification(submitted)
        wa_sent = ok
        wa_info = info
        if not ok:
            print("[WhatsApp]", info)

        return render_template("contact.html", success=True, name=name, wa_sent=wa_sent, wa_info=wa_info)

    return render_template("contact.html")
