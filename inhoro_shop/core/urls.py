from django.urls import path
from inhoro_shop.core.views import IndexView, NaturalPersonListView

app_name = 'core'
urlpatterns = [
    path('person/natural/', NaturalPersonListView.as_view(), name='natural_person_list'),
]
