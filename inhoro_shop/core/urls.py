from django.urls import path

from inhoro_shop.core.views import IndexView, NaturalPersonDetailView, NaturalPersonListView, LegalPersonDetailView, LegalPersonListView

app_name = 'core'
urlpatterns = [
    path('person/natural/<int:pk>', NaturalPersonDetailView.as_view(), name='natural_person'),
    path('person/natural/', NaturalPersonListView.as_view(), name='natural_person_list'),
    path('person/legal/<int:pk>', LegalPersonDetailView.as_view(), name='legal_person'),
    path('person/legal/', LegalPersonListView.as_view(), name='legal_person_list'),
]
