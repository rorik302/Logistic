from rest_framework.routers import SimpleRouter

from companies.views import CustomerViewSet, TransporterViewSet

router = SimpleRouter()
router.register("companies/customers", CustomerViewSet)
router.register("companies/transporters", TransporterViewSet)

urlpatterns = router.urls
