from django.urls import path, re_path, include

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    re_path(r'^webpush/', include('webpush.urls'))
]