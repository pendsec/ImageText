"""Imagetext URLs."""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('int/admin/', admin.site.urls),
    path('external/', include('external.urls'))
]
