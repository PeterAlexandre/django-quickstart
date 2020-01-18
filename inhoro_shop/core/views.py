from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DJLoginView
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView

from inhoro_shop.core.forms import NaturalPersonForm, LegalPersonForm
from inhoro_shop.core.models import NaturalPerson, LegalPerson


# General views
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


# User or authentication
class LoginView(DJLoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_redirect_url(self):
        url = super().get_redirect_url()
        if self.request.path == url:
            print('home')
            return reverse('home')
        return url


# LegalPerson
class LegalPersonCreateView(LoginRequiredMixin, CreateView):
    model = LegalPerson
    form_class = LegalPersonForm
    template_name = 'core/legal_person_create.html'

    def get_success_url(self):
        return reverse('core:legal_person_list')


class LegalPersonUpdateView(LoginRequiredMixin, UpdateView):
    model = LegalPerson
    form_class = LegalPersonForm
    template_name = 'core/legal_person_update.html'

    def get_success_url(self):
        return reverse('core:legal_person', kwargs={"pk": self.object.pk})


class LegalPersonDetailView(LoginRequiredMixin, DetailView):
    model = LegalPerson
    template_name = 'core/legal_person.html'
    context_object_name = 'legal_person'


class LegalPersonDeleteView(LoginRequiredMixin, DeleteView):
    model = LegalPerson
    template_name = 'core/legal_person_delete.html'
    context_object_name = 'legal_person'
    success_url = reverse_lazy('core:legal_person_list')


class LegalPersonListView(LoginRequiredMixin, ListView):
    model = LegalPerson
    template_name = 'core/legal_person_list.html'
    context_object_name = 'legal_person_list'


# NaturalPerson
class NaturalPersonCreateView(LoginRequiredMixin, CreateView):
    model = NaturalPerson
    form_class = NaturalPersonForm
    template_name = 'core/natural_person_create.html'

    def get_success_url(self):
        return reverse('core:natural_person_list')


class NaturalPersonUpdateView(LoginRequiredMixin, UpdateView):
    model = NaturalPerson
    form_class = NaturalPersonForm
    template_name = 'core/natural_person_update.html'

    def get_success_url(self):
        return reverse('core:natural_person', kwargs={"pk": self.object.pk})


class NaturalPersonDeleteView(LoginRequiredMixin, DeleteView):
    model = NaturalPerson
    template_name = 'core/natural_person_delete.html'
    context_object_name = 'natural_person'
    success_url = reverse_lazy('core:natural_person_list')


class NaturalPersonDetailView(LoginRequiredMixin, DetailView):
    model = NaturalPerson
    template_name = 'core/natural_person.html'
    context_object_name = 'natural_person'


class NaturalPersonListView(LoginRequiredMixin, ListView):
    model = NaturalPerson
    template_name = 'core/natural_person_list.html'
    context_object_name = 'natural_person_list'
