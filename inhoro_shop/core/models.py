from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        abstract = True


class Person(BaseModel):
    name = models.CharField(_('Name'), max_length=50)
    nickname = models.CharField(_('Nickname'), max_length=30)
    document = models.CharField(_('Document'), max_length=16)
    phone = models.CharField(_('Phone'), max_length=16)
    email = models.EmailField(_('Email'))


class LegalPerson(Person):
    person = models.OneToOneField('core.Person', on_delete=models.CASCADE, parent_link=True)
    state_registration = models.CharField(_('State registration'), max_length=18)
    municipal_registration = models.CharField(_('Municipal registration'), max_length=18)

    class Meta:
        verbose_name = _('Legal person')
        verbose_name_plural = _('Legal people')

    def __str__(self):
        return f'{self.document} - {self.name}'


class NaturalPerson(Person):
    GENDER = [('M', _('Male')), ('F', _('Female')), ('O', _('Other'))]

    person = models.OneToOneField('core.Person', on_delete=models.CASCADE, parent_link=True)
    birthday = models.DateField(_('Birthday'))
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDER)
    nationality = models.CharField(_('Nationality'), max_length=40)
    naturalness = models.CharField(_('Naturalness'), max_length=30)

    class Meta:
        verbose_name = _('Natural person')
        verbose_name_plural = _('Natural people')

    def __str__(self):
        return f'{self.document} - {self.name}'
