from rest_framework.routers import SimpleRouter

from companies.views import CompanyTypeViewSet

router = SimpleRouter()
router.register('types', CompanyTypeViewSet)

urlpatterns = []
urlpatterns += router.urls
