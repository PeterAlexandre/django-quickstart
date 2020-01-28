from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from inhoro_shop.api.v1.core.serializers import LegalPersonSerializer, NaturalPersonSerializer
from inhoro_shop.core.models import LegalPerson, NaturalPerson


class LegalPersonViewSet(ModelViewSet):
    queryset = LegalPerson.objects.order_by('pk')
    serializer_class = LegalPersonSerializer
    permission_classes = (IsAuthenticated,)


class NaturalPersonViewSet(ModelViewSet):
    queryset = NaturalPerson.objects.order_by('pk')
    serializer_class = NaturalPersonSerializer
    permission_classes = (IsAuthenticated,)
