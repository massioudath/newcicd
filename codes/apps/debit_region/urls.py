from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('region', views.DebitRegionViewSet, basename='region')
urlpatterns = [
   url(r'', include(router.urls)),
]
