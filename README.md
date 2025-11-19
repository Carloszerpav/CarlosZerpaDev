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
├── run.py                 # Punto de entrada
├── Procfile              # Comando para Railway
├── runtime.txt           # Versión de Python
└── requirements.txt      # Dependencias
```

## Notas
- La aplicación detecta automáticamente si está en desarrollo o producción
- En producción, los archivos estáticos tienen caché (1 hora)
- En desarrollo, no hay caché para facilitar el desarrollo

— Carloszerpav
