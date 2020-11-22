from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from companies.models import Company
from requests_app.models import Request
from requests_app.serializers import RequestSerializer


class RequestViewSet(ModelViewSet):
    queryset = Request.objects.select_related("customer__type_of_company").select_related("transporter__type_of_company")
    serializer_class = RequestSerializer

    def create(self, request, *args, **kwargs):
        instance = Request.objects.create(
            number=request.data['number'],
            customer=Company.objects.get(pk=request.data['customer']),
            transporter=Company.objects.get(pk=request.data['transporter']),
            loading_date=request.data['loading_date'],
            unloading_date=request.data['unloading_date'],
            loading_address=request.data['loading_address'],
            unloading_address=request.data['unloading_address'],
            customer_rate=request.data['customer_rate'],
            transporter_rate=request.data['transporter_rate']
        )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.number = request.data['number']
        instance.customer = Company.objects.get(pk=request.data['customer'])
        instance.transporter = Company.objects.get(pk=request.data['transporter'])
        instance.loading_date = request.data['loading_date']
        instance.unloading_date = request.data['unloading_date']
        instance.loading_address = request.data['loading_address']
        instance.unloading_address = request.data['unloading_address']
        instance.customer_rate = request.data['customer_rate']
        instance.transporter_rate = request.data['transporter_rate']
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)