from django.conf.urls import url
from . import views

app_name = 'energize_andover'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^display_choice/$', views.display_choice, name='display_choice')
]
