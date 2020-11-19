from rest_framework.serializers import ModelSerializer

from catalogs.types_of_companies.serializers import TypesOfCompaniesSerializer
from companies.models import Company


class CompanySerializer(ModelSerializer):
    type_of_company = TypesOfCompaniesSerializer(many=False)

    class Meta:
        model = Company
        fields = "__all__"
