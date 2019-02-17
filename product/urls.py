from django.urls import path
from .views import Onsale
from homepage.views import index

urlpatterns = [
    path('', index),
    path('<int:pro_id>/', Onsale.as_view(), name='product')
]
