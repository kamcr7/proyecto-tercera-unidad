# wsgi.py
import config.application as cfg

# intenta "application" y si no existe usa "app"
app = getattr(cfg, "application", None) or getattr(cfg, "app")