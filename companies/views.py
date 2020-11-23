from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from catalogs.types_of_companies.models import TypeOfCompany
from companies.models import Company
from companies.serializers import CompanySerializer


class CompaniesViewSet(ModelViewSet):
    queryset = Company.objects.select_related("type_of_company")
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            type_of_company = TypeOfCompany.objects.get(pk=request.data.pop('type_of_company'))
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        company = Company.objects.create(**request.data, type_of_company=type_of_company)
        return Response(CompanySerializer(company).data)

    def update(self, request, *args, **kwargs):
        try:
            type_of_company = TypeOfCompany.objects.get(pk=request.data.pop('type_of_company'))
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        company = Company.objects.get(pk=request.data['id'])
        company.type_of_company = type_of_company
        company.is_customer = request.data['is_customer']
        company.is_transporter = request.data['is_transporter']
        company.name = request.data['name']
        company.inn = request.data['inn']
        company.address = request.data['address']
        company.save()
        return Response(CompanySerializer(company).data)
