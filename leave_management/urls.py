from django.contrib import admin
from django.urls import path
from lm_app.views import login,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('', home),
]
