from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('notification/', include('notification.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^webpush/', include('webpush.urls'))
]