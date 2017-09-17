from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views as local_views
from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
    url(r'^create-user/$', local_views.UserCreate.as_view(), name='account-create'),
    url(r'^login/$', local_views.UserLogin.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
