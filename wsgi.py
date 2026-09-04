"""Punto de entrada WSGI para Vercel.

Vercel busca una instancia Flask llamada `app` en archivos reconocidos
(wsgi.py, app.py, index.py, etc.). Reexportamos la app creada en run.py.
"""

from run import app

__all__ = ["app"]
