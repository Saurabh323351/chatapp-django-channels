"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# mysite/urls.py
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from users.views import UserLogin, Registeration,stream,make_stream_response
urlpatterns = [
    path('',UserLogin.as_view(),name="login"),
    path('register/',Registeration.as_view(),name="register"),
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),

    # just trying to implement video streaming
    path('stream/',stream,name="stream"),
    path('stream_chunks/',make_stream_response,name="make_stream_response"),

]