from django.urls import path
from . import views

urlpatterns = [
    path('dashboared/', views.index, name='dashboared-index'),
    path('staff/', views.staff, name='dashboared-staff'),
    path('staff/detial/<int:pk>/', views.staff_detail,
         name='dashboared-staff-detail'),
    path('product/', views.product, name='dashboared-product'),
    path('product/delete/<int:pk>/', views.product_delete, 
         name='dashboared-product-delete'),
    path('product/update/<int:pk>/', views.product_update,
         name='dashboared-product-update'),
    path('order/', views.order, name='dashboared-order'),
]



"""
urlpatterns = [
    path('index/', views.index, name='dashboard-index'),
  ]

"""
