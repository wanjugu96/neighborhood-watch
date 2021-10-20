from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import  views
from django.urls.conf import path


urlpatterns = [
    url('^$',views.home,name='home'),
    url('^success$', views.success, name = 'success'),
    url('^createProfile$', views.createProfile,name='createProfile'),
    url('^uploadimage$', views.uploadimage,name='uploadimage'),
    path(r'^profile/<name>', views.profile,name='profile'),
    url(r'^image/(\d+)',views.singleimage , name='singleimage'),
    url(r'^image/(\d+)',views.updatelikes , name='singleimage')

    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
