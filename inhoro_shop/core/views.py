from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

from inhoro_shop.core.forms import NaturalPersonForm, LegalPersonForm
from inhoro_shop.core.models import NaturalPerson, LegalPerson


# General views
class IndexView(TemplateView):
    template_name = 'index.html'


# LegalPerson
class LegalPersonUpdateView(UpdateView):
    model = LegalPerson
    form_class = LegalPersonForm
    template_name = 'core/legal_person_update.html'

    def get_success_url(self):
        return reverse('core:legal_person', kwargs={"pk": self.object.pk})


class LegalPersonDetailView(DetailView):
    model = LegalPerson
    template_name = 'core/legal_person.html'
    context_object_name = 'legal_person'


class LegalPersonListView(ListView):
    model = LegalPerson
    template_name = 'core/legal_person_list.html'
    context_object_name = 'legal_person_list'


# NaturalPerson
class NaturalPersonUpdateView(UpdateView):
    model = NaturalPerson
    form_class = NaturalPersonForm
    template_name = 'core/natural_person_update.html'

    def get_success_url(self):
        return reverse('core:natural_person', kwargs={"pk": self.object.pk})


class NaturalPersonDetailView(DetailView):
    model = NaturalPerson
    template_name = 'core/natural_person.html'
    context_object_name = 'natural_person'


class NaturalPersonListView(ListView):
    model = NaturalPerson
    template_name = 'core/natural_person_list.html'
    context_object_name = 'natural_person_list'
