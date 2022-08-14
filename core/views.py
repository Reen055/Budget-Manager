from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Budget, Expense
from .forms import UserForm, BudgetForm, ExpenseForm


def home(request):
    return render(request, 'home.html')


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username,password= password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm(request, data=request.POST)

    return render(request, "login.html", {"form": form})


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,
                             'Your account has been created successfully')
            return redirect("login")
    else:
        form = UserForm()

    return render(request, "register.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have logout successfully")
    return redirect("home")

@login_required
def list_budgets(request):
    budgets = Budget.objects.all()
    context = {"budgets": budgets}
    return render(request, "list_budgets.html", context)


@login_required
def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Budget Added Successfully")
            return redirect('list_budgets')
    else:
        form = BudgetForm()

    return render(request, 'add_mod_budget.html', {
        "form": form,
        "title": "Add Budget"
    })

@login_required
def edit_budget(request, pk):
    budget = Budget.objects.get(pk=pk)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            messages.success(request, "Budget modified successfully")
            return redirect("list_budgets")
    else:
        form = BudgetForm(instance=budget)

    return render(request, "add_mod_budget.html", {
        "form": form,
        "title": "Edit Budget"
    })

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            budget = Budget.objects.get(pk=expense.budget.id)
            budget.amount -= expense.amount
            expense.save()
            budget.save()
            messages.success(request, "Expense added successfully")
            return redirect('list_expenses')
    else:
        form = ExpenseForm()

    return render(request, 'add_expense.html', {'form': form})


@login_required
def list_expenses(request):
    expenses = Expense.objects.all()
    context = {"expenses": expenses}
    return render(request, 'list_expenses.html', context)
