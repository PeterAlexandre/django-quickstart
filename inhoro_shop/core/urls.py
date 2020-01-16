from django.urls import path

from inhoro_shop.core import views


app_name = 'core'
urlpatterns = [
    # Legal URLs
    path('person/legal/create/', views.LegalPersonCreateView.as_view(), name='legal_person_create'),
    path('person/legal/<int:pk>/update/', views.LegalPersonUpdateView.as_view(), name='legal_person_update'),
    path('person/legal/<int:pk>', views.LegalPersonDetailView.as_view(), name='legal_person'),
    path('person/legal/', views.LegalPersonListView.as_view(), name='legal_person_list'),

    # Natural URLs
    path('person/natural/create/', views.NaturalPersonCreateView.as_view(), name='natural_person_create'),
    path('person/natural/<int:pk>/update/', views.NaturalPersonUpdateView.as_view(), name='natural_person_update'),
    path('person/natural/<int:pk>', views.NaturalPersonDetailView.as_view(), name='natural_person'),
    path('person/natural/', views.NaturalPersonListView.as_view(), name='natural_person_list'),
]
