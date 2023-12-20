"""qrgenvrest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from qrgen import qrgenerator
from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
     re_path(r'^api/start',qrgenerator.Normal_page),
      re_path(r'^api/home',qrgenerator.home),
      re_path(r'^api/send',qrgenerator.home),
      re_path(r'^api/wifi',qrgenerator.wifi_gen),
      re_path(r'^api/genwifi',qrgenerator.wifi_gen),
      re_path(r'^api/contactme',qrgenerator.contact_me),
      re_path(r'^api/makecontact',qrgenerator.contact_me),
      re_path(r'^api/bgimage',qrgenerator.image_bg),
      re_path(r'^api/imgbg',qrgenerator.image_bg),
      re_path(r'^api/logoimage',qrgenerator.logo_maker),
      re_path(r'^api/logosend',qrgenerator.logo_maker),
       re_path(r'^api/resumemaker',qrgenerator.resume_qr),
      re_path(r'^api/makeresume',qrgenerator.resume_qr),
] 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += staticfiles_urlpatterns() 