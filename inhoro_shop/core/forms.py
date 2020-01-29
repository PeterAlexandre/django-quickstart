from django import forms

from inhoro_shop.core.models import NaturalPerson, LegalPerson


class LegalPersonForm(forms.ModelForm):
    class Meta:
        model = LegalPerson
        exclude = ['created_at', 'updated_at']


class NaturalPersonForm(forms.ModelForm):
    class Meta:
        model = NaturalPerson
        exclude = ['created_at', 'updated_at']
