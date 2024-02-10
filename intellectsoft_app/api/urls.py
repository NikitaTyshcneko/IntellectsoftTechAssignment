from rest_framework import routers
from intellectsoft_app.views import ClientViewSet, RequestViewSet

router = routers.SimpleRouter()
router.register(r'clients', ClientViewSet)
router.register(r'requests', RequestViewSet)

urlpatterns = [

]

urlpatterns += router.urls
