from django.conf.urls import url
from trade.views import GoodList

urlpatterns = [
    url(r'^list', GoodList.as_view()),

]
