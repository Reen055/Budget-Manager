from django.contrib import admin
from .models import User, Expense, Budget

# Register your models here.
admin.site.register(User)
admin.site.register(Budget)
admin.site.register(Expense)