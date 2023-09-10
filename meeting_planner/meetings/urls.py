from django.urls import path
from . import views  # import your views

urlpatterns = [
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/', views.room_detail, name='room_detail'),
]