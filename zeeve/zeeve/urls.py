from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('modules.users.urls', namespace="users")),

    url(r'^admin/', admin.site.urls),
]
