from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("yurtici", views.yurtici),
    path('yurtdisi',views.yurtdisi),
    path('details/<int:id>', views.details, name='details'),
    path('advise',views.advise),
    path('advisedetails/<int:id>', views.advisedetail),
    path('create-text',views.create_text, name="create_text"),
    path('create-advise', views.create_advise, name="create_advise"),
    path('yazi-listesi',views.yazi_listesi, name="yazi_listesi"),
    
]