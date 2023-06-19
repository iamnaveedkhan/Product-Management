from django.urls import path
from productapp import views

urlpatterns =[
    path('add',views.add,name='add'),
    path('dashboard',views.dashboard, name='dash'),
    path('delete',views.delete),
    path('edit',views.edit),
]