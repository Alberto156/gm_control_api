from rest_framework import routers
from .views import UserViewSet

app_name = 'users'
router = routers.SimpleRouter()

router.register('', UserViewSet, basename='users')

urlpatterns = []

urlpatterns += router.urls