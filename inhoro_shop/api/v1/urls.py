from django.urls import path, include
from rest_framework.routers import DefaultRouter

from inhoro_shop.api.v1.core import views

router = DefaultRouter()

# App: core
router.register('legalperson', views.LegalPersonViewSet, basename='core.legal_person')
router.register('naturalperson', views.NaturalPersonViewSet, basename='core.natural_person')

app_name = 'v1'
urlpatterns = (
    path('', include(router.urls)),
)
