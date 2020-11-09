from rest_framework.routers import SimpleRouter

from catalogs.types_of_companies.views import TypesOfCompaniesViewSet

router = SimpleRouter()
router.register('types-of-companies', TypesOfCompaniesViewSet)

urlpatterns = router.urls