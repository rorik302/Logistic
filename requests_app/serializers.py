from rest_framework.serializers import ModelSerializer

from companies.serializers import CompanySerializer
from requests_app.models import Request


class RequestSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

    customer = CompanySerializer()
    transporter = CompanySerializer()
