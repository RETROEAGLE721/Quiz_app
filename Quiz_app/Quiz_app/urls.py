"""
URL configuration for Quiz_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.load_login, name="load_login"),
    path('load_page', view.load_page, name="load_page"),
    path('load_Signup', view.load_Signup, name="load_Signup"),
    path('user_answer', view.user_answer, name="user_answer"),
    path('index', view.index, name="index"),
    path('check_details', view.check_details, name="check_details"),
    path('save_details', view.save_details, name="save_details")
]
