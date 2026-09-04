"""Catálogo de proyectos del portfolio."""

from urllib.parse import quote

from flask import url_for

WHATSAPP_NUMBER = "56977979937"


def _whatsapp_url(message: str) -> str:
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"


def adobe_service_buttons() -> list[dict]:
    options = [
        (
            "Integraciones",
            "Conectamos Adobe con tus herramientas y sistemas para optimizar tus procesos.",
            "img/adobe-ps.png",
            "Hola, me interesa el servicio de Integraciones Adobe. Cuentan con experiencia en preventa y postventa, y quiero coordinar una conversación.",
        ),
        (
            "Webinars e inducciones",
            "Sesiones en vivo para capacitar equipos y asegurar una adopción efectiva.",
            "img/adobe-ai.png",
            "Hola, me interesa un Webinar o inducción de Adobe. Quiero conocer cómo lo abordan en preventa y postventa.",
        ),
        (
            "Training a usuarios",
            "Capacitaciones personalizadas según el rol y las necesidades de tu equipo.",
            "img/adobe-ai.png",
            "Hola, necesito training para usuarios de tecnologías Adobe. Me gustaría agendar una sesión.",
        ),
        (
            "Automatizaciones",
            "Diseñamos flujos y automatizaciones para ganar eficiencia y reducir tareas manuales.",
            "img/adobe-ps.png",
            "Hola, me interesa automatizar flujos con Adobe. Quiero revisar alcance, preventa y acompañamiento postventa.",
        ),
        (
            "PDF Services",
            "Implementación y soporte de soluciones PDF escalables, seguras y confiables.",
            "img/adobe-acr.png",
            "Hola, quiero información sobre Adobe PDF Services. Necesito apoyo técnico de preventa y postventa.",
        ),
        (
            "Firefly Services",
            "Integración y adopción de herramientas creativas con Adobe Firefly.",
            "img/adobe-fire.png",
            "Hola, me interesa Adobe Firefly Services. Quiero ver casos de uso y cómo pueden acompañarnos en preventa y postventa.",
        ),
        (
            "Soporte consola",
            "Acompañamiento y soporte continuo para administradores y usuarios.",
            "img/adobe-logo.png",
            "Hola, necesito soporte para usuarios y administradores de la consola Adobe. ¿Podemos coordinar una llamada?",
        ),
    ]
    return [
        {
            "label": label,
            "blurb": blurb,
            "icon": url_for("static", filename=icon),
            "url": _whatsapp_url(message),
        }
        for label, blurb, icon, message in options
    ]


def project_cards() -> list[dict]:
    return [
        {
            "title": "Servicios Adobe",
            "stack": ["Adobe", "PDF Services", "Firefly Services", "Automatización"],
            "desc": "Automatizaciones, configuraciones y training de innovación sobre el ecosistema Adobe. Experiencia técnica en PDF Services y Firefly Services para flujos documentales y creativos en entornos reales.",
            "url": "/proyectos/servicios-adobe",
            "category": "Adobe Services",
            "image": url_for("static", filename="img/adobe-logo.png"),
            "image_contain": True,
        },
        {
            "title": "DeporteMania",
            "stack": ["Web", "E-commerce", "Deporte"],
            "desc": "Sitio web en producción de DeporteMania: catálogo y venta de artículos deportivos, con experiencia de compra online para el público en Chile.",
            "url": "https://deportemania.cl/",
            "category": "Web App",
            "image": url_for("static", filename="img/deportemania-logo.png"),
            "image_contain": True,
            "is_external": True,
        },
        {
            "title": "Kaspersky Endpoint Security",
            "stack": ["Cybersecurity", "Enterprise", "Deployment", "Security Center"],
            "desc": "Despliegue y configuración de soluciones de seguridad Kaspersky para protección integral de sistemas empresariales. Implementación de Kaspersky Endpoint Security y gestión centralizada mediante Kaspersky Security Center.",
            "url": "/proyectos/kaspersky-endpoint-security",
            "category": "Security & Infrastructure",
            "image": "https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=800&h=400&fit=crop",
        },
        {
            "title": "App Trader",
            "stack": ["Frontend", "JavaScript", "Trading", "Real-time"],
            "desc": "Aplicación web frontend para traders con herramientas avanzadas de análisis de mercado y visualización de datos en tiempo real. Proyecto desarrollado con tecnologías modernas del lado del cliente, enfocado en una interfaz intuitiva y responsive para gestión de portafolios y seguimiento de activos.",
            "url": "/proyectos/app-trader",
            "category": "Frontend App",
            "image": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800&h=400&fit=crop",
        },
        {
            "title": "Sistema de Ventas",
            "stack": ["Python", "Flask", "PostgreSQL"],
            "desc": "Sistema integral de gestión de ventas con autenticación segura mediante Google OAuth. Plataforma eficiente para administrar transacciones, inventario y reportes en tiempo real.",
            "url": "/proyectos/sistema-ventas/",
            "category": "Web App",
            "image": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&h=400&fit=crop",
        },
        {
            "title": "Malva Shop",
            "stack": ["Catalog", "Web Design", "WhatsApp"],
            "desc": "Catálogo digital interactivo especializado en accesorios y maquillaje original. Plataforma diseñada para exhibir productos de manera elegante y profesional, con integración directa de contacto mediante WhatsApp e Instagram para facilitar la comunicación entre clientes y vendedora.",
            "url": "/proyectos/malva-shop/",
            "category": "Catalog Platform",
            "image": "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=800&h=400&fit=crop",
        },
    ]
