from django.urls import path, include

urlpatterns = [
    path('catalogs/', include('catalogs.urls'))
]