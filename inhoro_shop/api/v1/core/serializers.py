from rest_framework.serializers import ModelSerializer

from inhoro_shop.core.models import LegalPerson, NaturalPerson


class LegalPersonSerializer(ModelSerializer):
    class Meta:
        model = LegalPerson
        fields = ['id', 'name', 'document', 'phone', 'email', 'state_registration', 'municipal_registration']


class NaturalPersonSerializer(ModelSerializer):
    class Meta:
        model = NaturalPerson
        fields = ['id', 'name', 'document', 'phone', 'email', 'birthday', 'gender', 'nationality', 'naturalness']
