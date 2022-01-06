from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
# from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/',views.index, name='index'),
    path('register/', views.register, name='register'),
    path('',auth_views.LoginView.as_view(), name='login'),
    path('account/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)