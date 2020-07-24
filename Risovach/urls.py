from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView

from core.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='accounts_login'),
    path('', IndexView.as_view(), name='index'),
]
