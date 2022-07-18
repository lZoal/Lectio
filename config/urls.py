from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('notification/', include('notification.urls')),
    path('admin/', admin.site.urls),
]