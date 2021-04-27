from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    # Download path('admin/', admin.site.urls),
    ##path('', views.greeting, name='download-welcome'),
    # path('d2/', views.download2, name='d2'),
    path('', views.greetings , name="download-home"),
    path('download/', views.download),
    path('downloading/', views.downloading),
    path('sweet/', views.sweet)

]
