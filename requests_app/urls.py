from rest_framework.routers import SimpleRouter

from requests_app.views import RequestViewSet

router = SimpleRouter()
router.register('requests', RequestViewSet)

urlpatterns = router.urls
