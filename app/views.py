from django.shortcuts import render
from django.http import request

# Create your views here.


def SuperAdmin_index(request):
    return render(request,'SuperAdmin_index.html')

def SuperAdmin_Expense(request):
    return render(request,'SuperAdmin_Expense.html')

def SuperAdmin_ExpenseView(request):
    return render(request,'SuperAdmin_ExpenseView.html')

def SuperAdmin_NewTransaction(request):
    return render(request,'SuperAdmin_NewTransaction.html')

def SuperAdmin_ExpenseViewEdit(request):
    return render(request,'SuperAdmin_ExpenseViewEdit.html')

def SuperAdmin_FindExpense(request):
    return render(request,'SuperAdmin_FindExpense.html')

def SuperAdmin_FindExpenseView(request):
    return render(request,'SuperAdmin_FindExpenseView.html')

def SuperAdmin_FindExpenseViewEdit(request):
    return render(request,'SuperAdmin_FindExpenseViewEdit.html')

def SuperAdmin_FindExpenseNewTransaction(request):
    return render(request,'SuperAdmin_FindExpenseNewTransaction.html')