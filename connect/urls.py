from django.contrib import admin
from django.urls import path
import core.views


urlpatterns = [
    path('', core.views.home),
    path('admin/', admin.site.urls),
]