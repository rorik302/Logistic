from rest_framework.serializers import ModelSerializer

from catalogs.terms_of_payments.models import Term


class TermSerializer(ModelSerializer):
    class Meta:
        model = Term
        fields = "__all__"
