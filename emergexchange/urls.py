from django.conf.urls import url, include
from django.contrib import admin
import trade.urls
from trade import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'goods', views.GoodViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(trade.urls)),
    url(r'^api/v1/', include(router.urls, namespace='apiv1')),
]
