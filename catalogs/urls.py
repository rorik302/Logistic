from django.urls import path, include

urlpatterns = [
    path('', include('catalogs.types_of_companies.urls')),
    path('', include('catalogs.terms_of_payments.urls'))
]