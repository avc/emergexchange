from django.conf.urls import url
from trade.views import GoodList, FindMatches

urlpatterns = [
    url(r'^list', GoodList.as_view()),
    url(r'^test/(?P<uid>\d+)/$', FindMatches.as_view()),
    #url(r'^test/', views.FindMatches.as_view()),
]
