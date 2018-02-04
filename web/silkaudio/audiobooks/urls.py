from django.conf.urls import url, include
from audiobooks import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'audiobooks', views.AudiobookViewSet)
router.register(r'authors', views.AuthorViewSet)
# router.register(r'users', views.UserViewSet)
router.register(r'histories', views.HistoryViewSet, base_name='histories')

urlpatterns = [
    url(r'^', include(router.urls)),
]
