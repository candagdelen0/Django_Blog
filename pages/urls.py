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
    path('text-edit/<int:id>',views.text_edit, name="text_edit"),
    path('advise-edit/<int:id>', views.advise_edit, name="advise_edit"),
    
]