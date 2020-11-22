from django.urls import path, include

urlpatterns = [
    path('', include('catalogs.types_of_companies.urls'))
]