import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Carloszerpav: arranque configurado para Railway y desarrollo local
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "127.0.0.1")
    debug = os.environ.get("FLASK_ENV") == "development" or os.environ.get("DEBUG") == "True"
    
    print(f"Iniciando servidor Flask en http://{host}:{port} ...")
    app.run(host=host if host != "127.0.0.1" else "0.0.0.0", port=port, debug=debug)
