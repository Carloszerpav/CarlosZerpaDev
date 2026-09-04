"""Punto de entrada WSGI para Vercel."""

from werkzeug.middleware.dispatcher import DispatcherMiddleware

from apps.sistema_ventas.loader import load_ventas_app
from apps.sistema_ventas.paths import MOUNT_PREFIX
from run import app as portfolio_app

ventas_app = load_ventas_app()

app = DispatcherMiddleware(
    portfolio_app,
    {
        MOUNT_PREFIX: ventas_app,
    },
)
