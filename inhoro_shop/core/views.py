from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView

from inhoro_shop.core.forms import NaturalPersonForm, LegalPersonForm
from inhoro_shop.core.models import NaturalPerson, LegalPerson


# General views
class IndexView(TemplateView):
    template_name = 'index.html'


# LegalPerson
class LegalPersonCreateView(CreateView):
    model = LegalPerson
    form_class = LegalPersonForm
    template_name = 'core/legal_person_create.html'

    def get_success_url(self):
        return reverse('core:legal_person_list')


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


class LegalPersonDeleteView(DeleteView):
    model = LegalPerson
    template_name = 'core/legal_person_delete.html'
    context_object_name = 'legal_person'
    success_url = reverse_lazy('core:legal_person_list')


class LegalPersonListView(ListView):
    model = LegalPerson
    template_name = 'core/legal_person_list.html'
    context_object_name = 'legal_person_list'


# NaturalPerson
class NaturalPersonCreateView(CreateView):
    model = NaturalPerson
    form_class = NaturalPersonForm
    template_name = 'core/natural_person_create.html'

    def get_success_url(self):
        return reverse('core:natural_person_list')


class NaturalPersonUpdateView(UpdateView):
    model = NaturalPerson
    form_class = NaturalPersonForm
    template_name = 'core/natural_person_update.html'

    def get_success_url(self):
        return reverse('core:natural_person', kwargs={"pk": self.object.pk})


class NaturalPersonDeleteView(DeleteView):
    model = NaturalPerson
    template_name = 'core/natural_person_delete.html'
    context_object_name = 'natural_person'
    success_url = reverse_lazy('core:natural_person_list')


class NaturalPersonDetailView(DetailView):
    model = NaturalPerson
    template_name = 'core/natural_person.html'
    context_object_name = 'natural_person'


class NaturalPersonListView(ListView):
    model = NaturalPerson
    template_name = 'core/natural_person_list.html'
    context_object_name = 'natural_person_list'
