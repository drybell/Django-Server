from django.urls import include, path, re_path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet)

urlpatterns = [
	*router.urls,
]

