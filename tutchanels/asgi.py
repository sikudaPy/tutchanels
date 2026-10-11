# """
# ASGI config for tutchanels project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/
# """

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutchanels.settings')

# application = get_asgi_application()

# mysite/asgi.py


import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from chat.routing import websocket_urlpatterns
from channels.routing import URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutchanels.settings')
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
     {
         "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
#         # Just HTTP for now. (We can add other protocols later.)
     }
)

