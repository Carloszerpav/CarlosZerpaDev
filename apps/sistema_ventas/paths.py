"""Rutas montadas del Sistema de Ventas dentro del portfolio."""

MOUNT_PREFIX = "/proyectos/sistema-ventas"


def prefixed(path: str = "/") -> str:
    """Devuelve una ruta del sistema con el prefijo del portfolio."""
    if not path.startswith("/"):
        path = f"/{path}"
    if path == "/":
        return f"{MOUNT_PREFIX}/"
    return f"{MOUNT_PREFIX}{path}"
