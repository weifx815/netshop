"""netshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from common import views

urlpatterns = [
    # 前段访问 /common/menu/
    path('menu/list/', views.MenuList),
    path('menu/menuEdit/', views.menuEdit),
    path('menu/add/', views.menuAdd),
    path('menu/edit/<str:mid>', views.menuEdit),
    path('menu/view/<str:mid>/', views.menuView),
    path('menu/delete/<str:mid>/', views.menuDelete),
    path('role/list/', views.RoleList),
    path('role/add/', views.RoleAdd),
    path('role/edit/<str:rid>', views.RoleEdit),
    path('role/delete/<str:rid>/', views.RoleDelete),
    path('role/roleMenu/<str:rid>/', views.RoleMenu),
    path('role/saveRoleMenu/', views.SaveRoleMenu),
    path('role/addRole/<str:uid>/', views.addUserRole),
]
