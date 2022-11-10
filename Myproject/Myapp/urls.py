from django import views
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('myapp/', views.question_1,name='question_text'), 
    path('<int:id>',views.choice_list)

    #  path('',views.question_list,name='index'),

    # path('<int:id>',views.index,name='index')
]
