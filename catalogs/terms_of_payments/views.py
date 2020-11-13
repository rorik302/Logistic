from rest_framework.viewsets import ModelViewSet

from catalogs.terms_of_payments.models import Term
from catalogs.terms_of_payments.serializers import TermSerializer


class TermViewSet(ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
