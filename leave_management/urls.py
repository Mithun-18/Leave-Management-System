from django.contrib import admin
from django.urls import path
from lm_app.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
]
