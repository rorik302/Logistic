from rest_framework.serializers import ModelSerializer

from catalogs.types_of_companies.models import TypeOfCompany


class TypesOfCompaniesSerializer(ModelSerializer):
    class Meta:
        model = TypeOfCompany
        fields = "__all__"
