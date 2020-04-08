from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #url(r'^$', include('userLogin.urls')),
    url(r'^signup/', include('userLogin.urls')),
]
