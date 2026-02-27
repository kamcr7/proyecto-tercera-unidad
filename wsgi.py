from masonite.foundation import Application
from bootstrap import application

app = Application(application)
application = app.wsgi()