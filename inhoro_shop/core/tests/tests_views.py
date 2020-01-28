import datetime

from django.contrib.auth.views import REDIRECT_FIELD_NAME
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext as _
from model_mommy import mommy

from inhoro_shop.core.models import LegalPerson, NaturalPerson


class BaseTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('tester', password='testing')

    def not_anonymous(self, url):
        def test():
            self.client.logout()
            response = self.client.get(url)
            self.assertRedirects(response, f'{reverse("login")}?{REDIRECT_FIELD_NAME}={url}', status_code=302)
        return test

    def detail_view_test(self, model, url_name):
        self.client.force_login(self.user)
        lp = mommy.make(model)
        url = reverse(url_name, kwargs={'pk': lp.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertInHTML(lp.name, response.content.decode('utf8'))

    def list_view_test(self, model, url):
        self.client.force_login(self.user)
        mommy.make(model, _quantity=3)
        person = model.objects.values('name').first()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertInHTML(person['name'], response.content.decode('utf8'))


class IndexViewTest(BaseTestCase):
    url = reverse('home')

    def test_anonymous_user(self):
        self.not_anonymous(self.url)

    def test_logged_user(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertInHTML(_('Welcome to inhoro store!'), response.content.decode('utf8'))


class LegalPersonViewTest(BaseTestCase):
    # Anonymous tests
    def test_anonymous_user_create(self):
        self.not_anonymous(reverse('core:legal_person_create'))()

    def test_anonymous_user_detail(self):
        self.not_anonymous(reverse('core:legal_person', kwargs={'pk': mommy.make(LegalPerson).pk}))()

    def test_anonymous_user_list(self):
        mommy.make(LegalPerson, _quantity=3)
        self.not_anonymous(reverse('core:legal_person_list'))()

    def test_anonymous_user_update(self):
        self.not_anonymous(reverse('core:legal_person_update', kwargs={'pk': mommy.make(LegalPerson).pk}))()

    def test_anonymous_user_delete(self):
        self.not_anonymous(reverse('core:legal_person_update', kwargs={'pk': mommy.make(LegalPerson).pk}))()

    # view tests
    def test_create(self):
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
        self.assertRedirects(response, reverse('core:legal_person_list'), status_code=302)
        try:
            person = LegalPerson.objects.get(document=data['document'])
        except LegalPerson.DoesNotExist:
            self.fail('Legal person not created')
        except LegalPerson.MultipleObjectsReturned:
            self.fail('Legal person is duplicated')
        self.assertDictEqual(data, model_to_dict(person, fields=data.keys()))

    def test_detail(self):
        self.detail_view_test(LegalPerson, 'core:legal_person')

    def test_list(self):
        self.list_view_test(LegalPerson, reverse('core:legal_person_list'))

    def test_update(self):
        lp = mommy.make(LegalPerson).pk
        url = reverse('core:legal_person_update', kwargs={'pk': lp})
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
        self.assertRedirects(response, reverse('core:legal_person', kwargs={'pk': lp}))
        try:
            person = LegalPerson.objects.get(document=data['document'])
        except LegalPerson.DoesNotExist:
            self.fail('Legal person not updated')
        except LegalPerson.MultipleObjectsReturned:
            self.fail('Legal person is duplicated')
        self.assertDictEqual(data, model_to_dict(person, fields=data.keys()))

    def test_delete(self):
        lp = mommy.make(LegalPerson)
        url = reverse('core:legal_person_delete', kwargs={'pk': lp.pk})
        self.client.force_login(self.user)
        response = self.client.post(url)
        with self.assertRaises(LegalPerson.DoesNotExist):
            LegalPerson.objects.get(document=lp.document)
        self.assertRedirects(response, reverse('core:legal_person_list'), status_code=302)

    # error tests
    def test_detail_404(self):
        self.client.force_login(self.user)
        url = reverse('core:legal_person', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_empty_list(self):
        self.client.force_login(self.user)
        url = reverse('core:legal_person_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Sorry, no legal person in the list.', response.content.decode('utf8'))


class NaturalPersonViewTest(BaseTestCase):
    # Anonymous tests
    def test_anonymous_user_create(self):
        self.not_anonymous(reverse('core:natural_person_create'))()

    def test_anonymous_user_detail(self):
        self.not_anonymous(reverse('core:natural_person', kwargs={'pk': mommy.make(NaturalPerson).pk}))()

    def test_anonymous_user_list(self):
        mommy.make(NaturalPerson, _quantity=3)
        self.not_anonymous(reverse('core:natural_person_list'))()

    def test_anonymous_user_update(self):
        self.not_anonymous(reverse('core:natural_person_update', kwargs={'pk': mommy.make(NaturalPerson).pk}))()

    def test_anonymous_user_delete(self):
        self.not_anonymous(reverse('core:natural_person_update', kwargs={'pk': mommy.make(NaturalPerson).pk}))()

    # view tests
    def test_create(self):
        url = reverse('core:natural_person_create')
        self.client.force_login(self.user)
        data = {
            'name': 'testador',
            'nickname': 'Tes',
            'document': '06803958412',
            'phone': '82988909655',
            'email': 'testador@te.com',
            'birthday': datetime.date(1999, 2, 8),
            'gender': 'M',
            'nationality': 'Brasileiro',
            'naturalness': 'Maceió'
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('core:natural_person_list'), status_code=302)
        try:
            person = NaturalPerson.objects.get(document=data['document'])
        except NaturalPerson.DoesNotExist:
            self.fail('Natural person not created')
        except NaturalPerson.MultipleObjectsReturned:
            self.fail('Natural person is duplicated')
        self.assertDictEqual(data, model_to_dict(person, fields=data.keys()))

    def test_detail(self):
        self.detail_view_test(NaturalPerson, 'core:natural_person')

    def test_list(self):
        self.list_view_test(NaturalPerson, reverse('core:natural_person_list'))

    def test_update(self):
        np = mommy.make(NaturalPerson).pk
        url = reverse('core:natural_person_update', kwargs={'pk': np})
        self.client.force_login(self.user)
        data = {
            'name': 'testador',
            'nickname': 'Tes',
            'document': '06803958412',
            'phone': '82988909655',
            'email': 'testador@te.com',
            'birthday': datetime.date(1999, 2, 8),
            'gender': 'M',
            'nationality': 'Brasileiro',
            'naturalness': 'Maceió'
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('core:natural_person', kwargs={'pk': np}))
        try:
            person = NaturalPerson.objects.get(document=data['document'])
        except NaturalPerson.DoesNotExist:
            self.fail('Natural person not updated')
        except NaturalPerson.MultipleObjectsReturned:
            self.fail('Natural person is duplicated')
        self.assertDictEqual(data, model_to_dict(person, fields=data.keys()))

    def test_delete(self):
        np = mommy.make(NaturalPerson)
        url = reverse('core:natural_person_delete', kwargs={'pk': np.pk})
        self.client.force_login(self.user)
        response = self.client.post(url)
        with self.assertRaises(NaturalPerson.DoesNotExist):
            NaturalPerson.objects.get(document=np.document)
        self.assertRedirects(response, reverse('core:natural_person_list'), status_code=302)

    # error tests
    def test_detail_404(self):
        self.client.force_login(self.user)
        url = reverse('core:natural_person', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_empty_list(self):
        self.client.force_login(self.user)
        url = reverse('core:natural_person_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Sorry, no natural person in the list.', response.content.decode('utf8'))
