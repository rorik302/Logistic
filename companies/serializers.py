from rest_framework import serializers

from companies.models import CompanyType


class CompanyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyType
        fields = '__all__'
