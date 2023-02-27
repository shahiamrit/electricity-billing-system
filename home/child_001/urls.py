from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index, name='index'),
    path('dashboard', views.adminView, name='dashboard'),
    path('add', views.addCustomer, name='add'),
    path('bill', views.billCustomer, name='bill'),
    path('payment', views.paymentCustomer, name='payment'),
    path('viewCustomer', views.viewCustomer, name='viewCustomer'),
    path('viewCustomer/update/<int:pk>', views.viewUpdate, name='update'),
    path('deleteCustomer/delete/<int:pk>', views.viewDelete, name='delete'),
    path('addconnection', views.viewAddBill, name='addconnection'),
    path('addconnection/delete/<int:pk>', views.deleteAddConnection, name='del'),
]