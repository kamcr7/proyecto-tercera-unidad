import os

# Render/Heroku style: PORT is set by the platform
os.environ.setdefault("APP_ENV", os.getenv("APP_ENV", "production"))

from bootstrap.kernel import Kernel
from masonite.foundation import Application


# Create the Masonite application container
application = Application()

# Register the framework (routes, providers, etc.)
Kernel(application).register()

# Gunicorn looks for `app` by default in your command: gunicorn wsgi:app
app = application