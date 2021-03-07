
from django.contrib import admin
from django.urls import path ,include
from rest_framework import routers
from app.views import usrList,add_user
router = routers.DefaultRouter()
router.register(r'getUsers', usrList, basename="upload")
#router.register(r'addUser', add_user, basename="uploadd")
urlpatterns = [
    path('admin/', admin.site.urls),
       path('', include(router.urls)),
]
