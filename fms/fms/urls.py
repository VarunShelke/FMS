"""fms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.auth, name='auth'),
    path('login', views.login, name='login'),
    path('auto', views.auto, name='auto'),
    path('door_con', views.door_con, name='door_con'),
    path('gate_con', views.gate_con, name='gate_con'),
    path('fetch_data', views.fetch_data, name='fetch_data'),
    path('down_month_csv', views.down_month_csv, name='down_month_csv'),
    path('down_year_csv', views.down_year_csv, name='down_year_csv'),
    path('down_date_csv', views.down_date_csv, name='down_date_csv'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)