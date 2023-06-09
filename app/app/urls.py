"""
URL configuration for app project.

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

from admin_page.views import *

urlpatterns = [
    path('',index),
    path('chat/',chat),
    # path('admin/', admin.site.urls),
    path('admin/',admin_index),
    path('admin/login',admin_login),
    path('admin/logout',admin_logout),
    path('admin/users',admin_add_user),
    path('admin/delete/user/<id>',admin_delete_user),
    path('admin/update/user/<id>',admin_update_user),
    path('admin/profile',admin_profile),
    path('admin/profile/<id>/change/password',admin_change_password),
    path('admin/categories',admin_categories),
    path('admin/delete/category/<id>',admin_category_delete),
    path('admin/update/category/<id>',admin_category_update),
    path('admin/products',admin_products),
    path('admin/delete/product/<id>',admin_product_delete),
    path('admin/update/product/<id>',admin_product_update),


    
]
