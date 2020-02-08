from django.shortcuts import render

from .serializers import RegistrationSerializer,LoginSerializer
# from . models import Employee,Department
from django.views.generic import View
from django.http import HttpResponse,JsonResponse
import json,jwt
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView  # Added for Swagger to work
from django.contrib.sites.shortcuts import get_current_site
# from . utils import *
# from bitly_api import Connection,BitlyError, Error
import json
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name="dispatch")
class Registeration(GenericAPIView):

    serializer_class= RegistrationSerializer
    # permission_classes=(IsAuthenticated,)

    def post(self,request,*args,**kwargs):

        response = {'success': False,
                    'message': 'something went wrong',
                    'data': []
                    }

        request_data = json.loads(request.body)
        username=request_data["username"]
        password=request_data["password"]
        email=request_data["email"]
        user_obj=User(username=username,password=password,email=email)
        user_obj.set_password(password)
        # user_obj.is_active = False

        user_obj.save()

        # token=jwt.encode({"username":username},key="saurabhSecret",algorithm='HS256').decode('utf-8')
        # print(token,'-->')
        # subject="Email Verification"
        #
        # message="http://"+get_current_site(request).domain+"/"+"activate"+"/"+token
        #
        # API_USER = "o_1ucgrsfbmr"
        # API_KEY = "R_2d82deb00a324c4d9aa562de748135c0"
        # bitly = Connection(API_USER, API_KEY)
        #
        # bitly_response = bitly.shorten(message)
        #
        # print(bitly_response,'bitly_response-------->')
        #
        #
        # message=bitly_response['url']

        # message=render_to_string('serializerApp/account_activate.html',{
        #     "token":token,
        #     "domain":get_current_site(request).domain
        # })
        #
        # print(message)

        # to="singh.saurabh3333@gmail.com"
        # recipient_list=[to]
        # status=send_mail(subject,message,'singh.saurabh3333@gmail.com',[to])
        # print(status,'----status')
        # status=ee.emit('event',subject,message,recipient_list)
        # print(status)
        response['success']=True
        response['message']="Registeration successful"

        return JsonResponse(response)

def activate(request,token):

    response = {'success': False,
                'message': 'something went wrong',
                'data': []
                }

    payload=jwt.decode(token,key="saurabhSecret",algorithms=['HS256'])
    print(payload)
    username=payload["username"]
    obj=User.objects.get(username=username)

    if obj.is_active is not True:
        obj.is_active=True
        obj.save()

        response['success'] = True
        response['message'] = "account verified successfully"

    else:
        response['success'] = False
        response['message'] = "account already verified"

    return JsonResponse(response)


from django.contrib.auth import authenticate


@method_decorator(csrf_exempt,name="dispatch")
class UserLogin(GenericAPIView):

    serializer_class = LoginSerializer
    # permission_classes=(AllowAny,)
    def get(self, request, *args, **kwargs):

        return render(request,'users/login.html',{})

    def post(self,request,*args,**kwargs):

        try:

            print(request.data,'---->request.data')
            response={
                'success':False,
                'message':'something went wrong',
                'data':[]
            }

            request_data=(request.data) # it is giving dict

            print(request_data,'request_data------>',type(request_data))

            username=request_data['username']
            password=request_data['password']
            #
            # user_obj = User(username=username, password=password)
            # user_obj.set_password(password)
            # # user_obj.is_active = False
            #
            # user_obj.save()

            user_obj=authenticate(username=username,password=password)
            print(user_obj,'-----user_obj')
            payload={'id':user_obj.id}
            token=jwt.encode(payload=payload,key="its a secret",algorithm='HS256').decode('utf-8')

            response['success']=True
            response['message']='successfully logged in'
            response['data']={'token':token}

            response=json.dumps(response)

        except User.DoesNotExist:

            response=response['message'] = 'User Does Not Exist'
            response=json.dumps(response)

        return HttpResponse(response)


from django.http import StreamingHttpResponse


def stream(request):

    # in this case i am trying to stream whole video at once
    # in this whole video is loaded to memory at once then it going for serving
    # due to this ,on server has lots of loads
    with open('./video/Get-Python-Installed.mp4', 'rb') as video_file:
        response = HttpResponse(video_file.read(), content_type='video/mp4')
        response['Content-Disposition'] = 'inline; filename=%s' % 'video.mp4'
        return response
    video_file.close()


def make_stream_response(file_path="./video/Get-Python-Installed.mp4", content_type='video/mp4', file_size=24036666, attachment=None):

    # Now this method ,i am trying to serve chunk by chunk of video data
    # so chuck by chunk video data will load into memory then that chuck will be serve
    response = StreamingHttpResponse(open("./video/Get-Python-Installed.mp4", 'rb'))

    response['Content-Type'] = content_type
    response['Content-Length'] = file_size
    if attachment:
        header = 'attachment; filename="%s"' % attachment
        response['Content-Disposition'] = header

    return response


