from django.contrib import admin
from django.urls import path
import core.views
from records.views import subscribe


urlpatterns = [
    path('', core.views.home),
    path('register/', subscribe),
    path('admin/', admin.site.urls),
]