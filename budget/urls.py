"""budget URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from core.views import home, login_page, register, add_budget, add_expense, list_budgets, list_expenses, edit_budget, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path("add_budget/", add_budget, name="add_budget"),
    path("list_budgets/", list_budgets, name="list_budgets"),
    path('add_expense/', add_expense, name='add_expense'),
    path('list_expenses/', list_expenses, name='list_expenses'),
]
