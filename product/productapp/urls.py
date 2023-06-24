from django.urls import path
from productapp import views

urlpatterns =[
    path('add',views.add),
    path('dashboard',views.dashboard),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
]