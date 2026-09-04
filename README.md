# Portfolio Flask - Carlos Zerpa

Proyecto base en Flask para portfolio, blog y servicios.

## Requisitos
- Python 3.11+

## Instalación Local

### 1. Crear entorno virtual
**PowerShell:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**CMD:**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

### 2. Instalar dependencias
```cmd
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Ejecutar en desarrollo
```cmd
python run.py
```

La aplicación estará disponible en: http://127.0.0.1:5000

## Despliegue en Vercel

1. En [vercel.com/new](https://vercel.com/new) importa el repo `Carloszerpav/CarlosZerpaDev`.
2. Usa estos valores en el dashboard (el repo ya incluye `vercel.json`, `wsgi.py` y `pyproject.toml`):

| Campo | Valor |
|---|---|
| Framework Preset | Other / Flask (si aparece) |
| Root Directory | `.` |
| Build Command | vacío |
| Output Directory | vacío |
| Install Command | `pip install -r requirements.txt` |
| Production Branch | `main` |

3. En **Settings → General**, deja Python **3.12** (archivo `.python-version`). Railway sigue usando 3.11 vía `runtime.txt`.
4. Variables de entorno (Production y Preview):
   - `FLASK_ENV=production`
   - WhatsApp si las usas (ver sección WhatsApp)

Vercel no usa el `Procfile` ni Gunicorn: corre Flask como una función serverless a través de `wsgi.py`.

## Despliegue en Railway

### Pasos para desplegar:

1. **Conectar repositorio:**
   - Crea una cuenta en [Railway](https://railway.app)
   - Crea un nuevo proyecto
   - Conecta tu repositorio de GitHub/GitLab

2. **Configurar variables de entorno (opcional):**
   En Railway, ve a Variables y agrega:
   - `FLASK_ENV=production`
   - Variables de WhatsApp si las necesitas (ver sección WhatsApp)

3. **Deploy automático:**
   - Railway detectará automáticamente el `Procfile`
   - La aplicación se desplegará automáticamente
   - Railway asignará un puerto automáticamente (variable `PORT`)

### Archivos de configuración para Railway:
- `Procfile` - Define el comando de inicio
- `runtime.txt` - Especifica la versión de Python
- `requirements.txt` - Dependencias del proyecto

## WhatsApp (opcional)
- Crea un archivo `.env` en la raíz con tus credenciales (solo para desarrollo local).
- En Railway, usa las Variables de Entorno.

**Opción Cloud API (Meta):**
```
WA_PROVIDER=cloud
WHATSAPP_CLOUD_TOKEN=...
WHATSAPP_PHONE_NUMBER_ID=...
WHATSAPP_TO=whatsapp:+58XXXXXXXXXX
```

**Opción Twilio (sandbox):**
```
WA_PROVIDER=twilio
TWILIO_ACCOUNT_SID=...
TWILIO_AUTH_TOKEN=...
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
WHATSAPP_TO=whatsapp:+58XXXXXXXXXX
```

## Estructura
```
CarlosZerpaDev/
├── app/                    # Código fuente
│   ├── templates/         # HTML con Jinja2
│   ├── static/            # Archivos estáticos
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   ├── __init__.py        # Factory de Flask
│   └── routes.py          # Rutas de la aplicación
├── run.py                 # Punto de entrada local / Railway
├── wsgi.py                # Punto de entrada WSGI para Vercel
├── vercel.json            # Configuración de funciones Vercel
├── pyproject.toml         # Entrypoint Vercel (wsgi:app)
├── .python-version        # Python 3.12 en Vercel
├── Procfile              # Comando para Railway
├── runtime.txt           # Versión de Python en Railway
└── requirements.txt      # Dependencias
```

## Notas
- La aplicación detecta automáticamente si está en desarrollo o producción
- En producción, los archivos estáticos tienen caché (1 hora)
- En desarrollo, no hay caché para facilitar el desarrollo

— Carloszerpav
