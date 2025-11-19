import os
from flask import Flask

try:
    from dotenv import load_dotenv
except Exception:
    load_dotenv = None


def create_app() -> Flask:
    """Crea y configura la app Flask.
    Nota rápida by Carloszerpav: mantenemos esto simple para empezar.
    """
    if load_dotenv:
        load_dotenv()
    app = Flask(__name__)

    # Determinar si estamos en desarrollo o producción
    is_development = os.environ.get("FLASK_ENV") == "development" or os.environ.get("DEBUG") == "True"
    
    # Configuración de caché
    if is_development:
        # Evitar caché agresivo en desarrollo
        app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    else:
        # Caché normal en producción (1 hora para archivos estáticos)
        app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 3600

    @app.after_request
    def add_no_cache_headers(response):
        # Sólo para desarrollo: fuerza al navegador a no cachear
        if is_development:
            response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
            response.headers["Pragma"] = "no-cache"
        return response

    # Registro de rutas
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
