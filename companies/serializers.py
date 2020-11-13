from rest_framework.serializers import ModelSerializer

from catalogs.types_of_companies.serializers import TypesOfCompaniesSerializer
from companies.models import Company


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

    type_of_company = TypesOfCompaniesSerializer()
