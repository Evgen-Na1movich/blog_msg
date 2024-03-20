"""
URL configuration for sitewomen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from women import views
from women.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),  # http://127.0.0.1:8000/
    path("__debug__/", include("debug_toolbar.urls")),
    path('users/', include('users.urls', namespace='users')),
    # Параметр namespace, который позволяет формировать пространство имен для доступа к URL-маршрутам.
    # Например, сейчас для доступа к маршруту http://127.0.0.1:8000/users/login/
    # достаточно будет обратиться по его имени с указанием пространства имен users следующим образом:
    # users:login
    # Таким образом, мы дополнительно изолируем приложение users от возможных конфликтов в именах маршрутов
    # других приложений


]

handler404 = page_not_found

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Известные женщины мира"
