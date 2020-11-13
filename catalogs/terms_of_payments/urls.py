from rest_framework.routers import SimpleRouter

from catalogs.terms_of_payments.views import TermViewSet

router = SimpleRouter()
router.register('terms-of-payments', TermViewSet)

urlpatterns = router.urls
