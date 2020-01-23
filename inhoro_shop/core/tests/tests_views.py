from django.contrib.auth.views import REDIRECT_FIELD_NAME
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext as _
from model_mommy import mommy

from inhoro_shop.core.models import LegalPerson


class BaseTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('tester', password='testing')


class IndexViewTestCase(BaseTestCase):
    url = reverse('home')

    def test_anonymous_user_get(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, f'{reverse("login")}?{REDIRECT_FIELD_NAME}={self.url}')

    def test_logged_user(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertInHTML(_('Welcome to inhoro store!'), response.content.decode('utf8'))


class LegalPersonViewTestCase(BaseTestCase):
    def test_anonymous_user_create(self):
        url = reverse('core:legal_person_create')
        response = self.client.get(url)
        self.assertRedirects(response, f'{reverse("login")}?{REDIRECT_FIELD_NAME}={url}')

    def test_user_create(self):
        url = reverse('core:legal_person_create')
        self.client.force_login(self.user)
        data = {
            'name': 'Tester',
            'nickname': 'Test',
            'document': '85296374115',
            'phone': '11988929655',
            'email': 'tester@te.com',
            'state_registration': 'AL',
            'municipal_registration': 'Maceió'
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('core:legal_person_list'))
        try:
            person = LegalPerson.objects.get(document=data['document'])
        except LegalPerson.DoesNotExist:
            self.fail('Legal person not created')
        except LegalPerson.MultipleObjectsReturned:
            self.fail('Legal person is duplicated')
        self.assertDictEqual(data, model_to_dict(person, fields=data.keys()))

    def test_detail(self):
        self.client.force_login(self.user)
        lp = mommy.make(LegalPerson)
        url = reverse('core:legal_person', kwargs={'pk': lp.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertInHTML(lp.name, response.content.decode('utf8'))
