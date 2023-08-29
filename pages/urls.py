from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("yurtici", views.yurtici),
    path('yurtdisi',views.yurtdisi),
    path('details/<int:id>', views.details, name='details'),
]