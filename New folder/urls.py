from . import views
from django.urls import re_path

urlpatterns=[  
    
    re_path(r'^SuperAdmin_index$',views.SuperAdmin_index,name='SuperAdmin_index'),
    re_path(r'^SuperAdmin_Expense$',views.SuperAdmin_Expense,name='SuperAdmin_Expense'),
    re_path(r'^SuperAdmin_ExpenseView$',views.SuperAdmin_ExpenseView,name='SuperAdmin_ExpenseView'),
    re_path(r'^SuperAdmin_NewTransaction$',views.SuperAdmin_NewTransaction,name='SuperAdmin_NewTransaction'),
    re_path(r'^SuperAdmin_ExpenseViewEdit$',views.SuperAdmin_ExpenseViewEdit,name='SuperAdmin_ExpenseViewEdit'),
    re_path(r'^SuperAdmin_FindExpense$',views.SuperAdmin_FindExpense,name='SuperAdmin_FindExpense'),
    re_path(r'^SuperAdmin_FindExpenseView$',views.SuperAdmin_FindExpenseView,name='SuperAdmin_FindExpenseView'),
    re_path(r'^SuperAdmin_FindExpenseViewEdit$',views.SuperAdmin_FindExpenseViewEdit,name='SuperAdmin_FindExpenseViewEdit'),
    re_path(r'^SuperAdmin_FindExpenseNewTransaction$',views.SuperAdmin_FindExpenseNewTransaction,name='SuperAdmin_FindExpenseNewTransaction'),
]