from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from inhoro_shop.core.models import NaturalPerson, LegalPerson


# General views
class IndexView(TemplateView):
    template_name = 'index.html'


# LegalPerson
class LegalPersonDetailView(DetailView):
    model = LegalPerson
    template_name = 'core/legal_person.html'


class LegalPersonListView(ListView):
    template_name = 'core/legal_person_list.html'
    model = LegalPerson


# NaturalPerson
class NaturalPersonDetailView(DetailView):
    model = NaturalPerson
    template_name = 'core/natural_person.html'


class NaturalPersonListView(ListView):
    template_name = 'core/natural_person_list.html'
    model = NaturalPerson
