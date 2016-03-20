from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^energize_andover/', include('energize_andover.urls')),
    url(r'^admin/', admin.site.urls),
]
