from django.contrib import admin
from django.urls import path

from thread.views import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')


urlpatterns = router.urls
urlpatterns += path('admin/', admin.site.urls),
