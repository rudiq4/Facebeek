from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'general'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tastes/$', views.tastes, name='tastes'),
    url(r'^about/$', views.about, name='about'),
    url(r'^catering/$', views.catering, name='catering'),

]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)