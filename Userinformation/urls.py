from django.urls import path 
from . import views




urlpatterns = [
    path('',views.userinfo,name='userinfo'),
    path('delete/<uuid:id>/', views.delete, name='delete'),
    path('update/<uuid:id>/',views.update,name='update'),

]