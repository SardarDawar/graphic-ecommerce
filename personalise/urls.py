from django.urls import path
from . import views

urlpatterns = [
    path('personalise/<product_id>', views.personalise, name='personalise'),
]
