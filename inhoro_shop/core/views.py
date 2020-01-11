from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from inhoro_shop.core.models import NaturalPerson


class IndexView(TemplateView):
    template_name = 'index.html'


class NaturalPersonListView(ListView):
    template_name = 'core/naturalperson.html'
    model = NaturalPerson
