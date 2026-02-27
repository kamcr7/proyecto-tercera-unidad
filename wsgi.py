# wsgi.py
import os

from masonite.foundation import App
from Kernel import Kernel

# (opcional pero recomendado)
os.environ.setdefault("APP_ENV", "production")

# crea la app
application = App()

# registra el kernel (carga config, rutas, middleware, etc.)
Kernel(application).register()

# gunicorn necesita "app"
app = application