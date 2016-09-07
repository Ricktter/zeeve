from django.conf.urls import url
from .views import index, userlogin, LogOut

urlpatterns = [
    url(r'^$', index),
    url(r'^login/$', userlogin, name="login"),
    url(r'^salir/$', LogOut, name='logout')
]
