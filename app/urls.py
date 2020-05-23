from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.landing, name='landing'),
    url(r'^car_list/$', views.car_listing, name='car_list'),
    url(r'^car_details/$', views.car_details, name='car_details'),
    url(r'^blog/$', views.blog_list, name='blog_list'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)