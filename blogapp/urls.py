from . import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
  path('', views.home, name='home'),
  path('about', views.about, name='about'),
  path('contact', views.contact, name='contact')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)