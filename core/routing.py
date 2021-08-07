from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

#'application' is very similar to 'urlpatterns'
application = ProtocolTypeRouter({
    #Now we wrap our routers inside the AuthMiddlewareStack so as to utilise the built-in authentication provided by django. 
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )

})