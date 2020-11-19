from rest_framework.routers import SimpleRouter

from companies.views import CompaniesViewSet

router = SimpleRouter()
router.register("companies", CompaniesViewSet)

urlpatterns = router.urls
