from django.conf.urls import url, include
from django.conf.urls.i18n import urlpatterns
from rest_framework import routers
from tests.testapp import router

from apps import views
from apps.views import Index

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^api/$', include(router.urls)),
    url(r'^api-auth/$', include('rest_framework.urls'))
]