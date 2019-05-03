from django.contrib import admin
from django.urls import path , include

from blog.views import *
from .views import home
from accounts.views import login_view, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djusers/home/', home),
    path('accounts/login/', login_view),
    path('accounts/register/', register_view),
    path('accounts/logout/', logout_view),
    path('',home),
    path('blog/about/', about),
    path('blog/addasseth/',addasseth),
    path('blog/ProjectDetailh/', ProjectDetailh),
    path('blog/AddProjectDocumenth/',AddProjectDocumenth),
]
