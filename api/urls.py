from django.urls import path, include

urlpatterns = [
    path('catalogs/', include('catalogs.urls')),
    path('', include('companies.urls')),
    path('', include('requests_app.urls'))
]