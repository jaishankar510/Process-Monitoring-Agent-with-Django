

# from rest_framework.routers import DefaultRouter
# from .views import SystemInfoViewSet, ProcessInfoViewSet

# router = DefaultRouter()
# router.register('systeminfo', SystemInfoViewSet, basename='systeminfo')
# router.register('processinfo', ProcessInfoViewSet, basename='processinfo')

# urlpatterns = router.urls




from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SystemInfoViewSet, ProcessInfoViewSet
from . import views

router = DefaultRouter()
router.register(r'systeminfo', SystemInfoViewSet, basename='systeminfo')
router.register(r'processinfo', ProcessInfoViewSet, basename='processinfo')

urlpatterns = [
    path('api/', include(router.urls)),
    path('frontend/', views.index, name="index")

]
