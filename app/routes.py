from flask import Blueprint, render_template, request, send_from_directory
import os

from .catalog import project_cards

MALVA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "apps", "malva")

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
    return render_template("projects.html", projects=project_cards())


@bp.get("/proyectos/malva-shop")
@bp.get("/proyectos/malva-shop/")
def malva_shop_index():
    return send_from_directory(MALVA_DIR, "index.html")


@bp.get("/proyectos/malva-shop/<path:filename>")
def malva_shop_file(filename: str):
    return send_from_directory(MALVA_DIR, filename)


@bp.get("/proyectos/servicios-adobe")
def adobe_services():
    return render_template(
        "adobe_services.html",
        title="Servicios Adobe | Carlos Zerpa",
    )


@bp.get("/proyectos/app-trader")
def app_trader():
    return render_template(
        "project_info.html",
        title="App Trader | Carlos Zerpa",
        heading="App Trader",
        desc="Aplicación frontend para traders con análisis de mercado y visualización en tiempo real. Pensada para uso en dispositivo, con interfaz intuitiva y seguimiento de activos.",
    )


@bp.get("/proyectos/kaspersky-endpoint-security")
def kaspersky_endpoint():
    return render_template(
        "project_info.html",
        title="Kaspersky Endpoint Security | Carlos Zerpa",
        heading="Kaspersky Endpoint Security",
        desc="Despliegue y configuración de Kaspersky Endpoint Security y gestión centralizada con Kaspersky Security Center en entorno empresarial.",
    )


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
