from django.urls import path

from . import views
app_name='base'
urlpatterns = [
    path('',views.index, name="index"),
    path('add-rental/',views.create_rental_property, name="create-rental"),
    path('add-sale/',views.create_sale_property, name="create-sale"),
  
]