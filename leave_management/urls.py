from django.contrib import admin
from django.urls import path
from lm_app.views import login,home,logout,leave_info,action,cancel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('logout/', logout),
    path('', home),
    path('leaves/', leave_info),
    path('action/', action),
    path('cancel/', cancel),
]
