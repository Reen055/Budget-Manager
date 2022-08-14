from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Budget Model
class Budget(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} : {self.amount}"

# Expense model

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.amount} - {self.budget}"

