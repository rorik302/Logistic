from rest_framework.viewsets import ModelViewSet

from requests_app.models import Request
from requests_app.serializers import RequestSerializer


class RequestViewSet(ModelViewSet):
    queryset = Request.objects.select_related("customer__type_of_company").select_related("transporter__type_of_company")
    serializer_class = RequestSerializer
