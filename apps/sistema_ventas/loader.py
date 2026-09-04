"""Carga la app Flask de Sistema de Ventas sin chocar con el paquete `app` del portfolio."""

from __future__ import annotations

import importlib.util
import os
import sys

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_ventas_app():
    if _BASE_DIR not in sys.path:
        sys.path.insert(0, _BASE_DIR)

    app_file = os.path.join(_BASE_DIR, "app.py")
    spec = importlib.util.spec_from_file_location("sistema_ventas_wsgi", app_file)
    if spec is None or spec.loader is None:
        raise RuntimeError("No se pudo cargar apps/sistema_ventas/app.py")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.app
