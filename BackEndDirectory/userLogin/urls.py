from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   url(r'^$', views.UserFormView.as_view(), name='register'),
]

urlpatterns += staticfiles_urlpatterns()