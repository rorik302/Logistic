from rest_framework.viewsets import ModelViewSet

from companies.models import Company
from companies.serializers import CompanySerializer


class CustomerViewSet(ModelViewSet):
    queryset = Company.objects.filter(is_customer=True).select_related("type_of_company")
    serializer_class = CompanySerializer


class TransporterViewSet(ModelViewSet):
    queryset = Company.objects.filter(is_transporter=True).select_related("type_of_company")
    serializer_class = CompanySerializer
