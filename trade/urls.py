from django.conf.urls import url
from trade.views import GoodList, FindMatches

urlpatterns = [
    url(r'^list', GoodList.as_view()),
    url(r'^trades/(?P<uid>\d+)/$', FindMatches.as_view()),
]
