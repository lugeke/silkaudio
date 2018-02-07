from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from django.utils.translation import ugettext_lazy as _

from audiobooks import views

router = DefaultRouter()
router.register(r'audiobooks', views.AudiobookViewSet)
router.register(r'authors', views.AuthorViewSet)
# router.register(r'users', views.UserViewSet)
# router.register(r'histories', views.HistoryViewSet, base_name='histories')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(_(r'^history/$'),  # (?P<audiobook>\d+)/
        views.HistoryView.as_view(),
        name='history'),
]
