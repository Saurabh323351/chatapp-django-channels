from django.utils.deprecation import MiddlewareMixin
import jwt
from django.conf import settings
from django.contrib.auth.models import User

class BookMiddleware(MiddlewareMixin):


    def process_view(self, request, view_func, view_args, view_kwargs):

        # request.META.get('HTTP_AUTHORIZATION')
        print("executed------>")

        # token_scheme = request.META.get('HTTP_AUTHORIZATION')
        token=request.META.get('HTTP_AUTHORIZATION')

        if token is not None:
            # token_list=token_scheme.split(' ')
            # print(token_list[1])

            payload=jwt.decode(token,key="its a secret")
            print(payload,'---------->payload')
            user_obj=User.objects.get(id=payload['id'])

            request.user=user_obj
            print(request.user,'---------->middleware')



