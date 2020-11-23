from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from catalogs.types_of_companies.models import TypeOfCompany
from catalogs.types_of_companies.serializers import TypesOfCompaniesSerializer


class TypesOfCompaniesViewSet(ModelViewSet):
    queryset = TypeOfCompany.objects.all()
    serializer_class = TypesOfCompaniesSerializer
    permission_classes = [IsAuthenticated]
