from channels.auth import AuthMiddlewareStack
from django.contrib.auth.models import AnonymousUser,User
import jwt,pprint
from django.db import close_old_connections

class TokenAuthMiddleware:
    """
    JWT-Token authorization middleware for Django Channels 2
    """

    def __init__(self, inner):
        self.inner = inner

        print(inner,'------->inner')
    def __call__(self, scope):

        # pprint.pprint(scope, indent=4)
        # headers = dict(scope['headers'])
        print(scope['query_string'],'query_string,__call__')
        token=(scope['query_string'])
        payload=jwt.decode(token,'secret',algorithms=['HS256'])
        print(payload)
        user_obj=User.objects.get(id=payload['id'])
        scope["user"] = user_obj
        close_old_connections()

        # print(scope['user'])

        # if b'authorization' in headers:
        #     try:
        #         token_name, token_key = headers[b'authorization'].decode().split()
        #         if token_name == 'Token':
        #             token = Token.objects.get(key=token_key)
        #             scope['user'] = token.user
        #     except Token.DoesNotExist:
        #         scope['user'] = AnonymousUser()

        return self.inner(scope)

TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))
