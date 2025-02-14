from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Show the input form
    path('predict/', views.predict_price, name='predict_price'),  # Handle the prediction
]
