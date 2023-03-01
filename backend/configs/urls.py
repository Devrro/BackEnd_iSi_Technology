"""configs URL Configuration

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
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_token', TokenObtainPairView.as_view(), name='obtain_token_view'),
    path('refresh_token', TokenRefreshView.as_view(), name='refresh_token_view'),
    path('users', include('apps.users.urls'), name='users_url'),
    path('chats', include('apps.simple_chat.urls'), name='message_url')
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
handler500 = 'rest_framework.exceptions.server_error'
handler400 = 'rest_framework.exceptions.bad_request'
