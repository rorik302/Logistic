from rest_framework.viewsets import ModelViewSet

from companies.models import CompanyType
from companies.serializers import CompanyTypeSerializer


class CompanyTypeViewSet(ModelViewSet):
    queryset = CompanyType.objects.all()
    serializer_class = CompanyTypeSerializer
