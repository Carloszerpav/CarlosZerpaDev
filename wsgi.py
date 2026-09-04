"""Punto de entrada WSGI para Vercel.

El portfolio Flask convive con Sistema de Ventas bajo /proyectos/sistema-ventas.
"""

import importlib.util
import os

from werkzeug.middleware.dispatcher import DispatcherMiddleware

from run import app as portfolio_app

_ROOT = os.path.dirname(os.path.abspath(__file__))
_VENTAS_FILE = os.path.join(_ROOT, "apps", "sistema_ventas", "app.py")
_spec = importlib.util.spec_from_file_location("sistema_ventas_wsgi", _VENTAS_FILE)
_ventas_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_ventas_mod)
ventas_app = _ventas_mod.app

app = DispatcherMiddleware(
    portfolio_app,
    {
        "/proyectos/sistema-ventas": ventas_app,
    },
)
