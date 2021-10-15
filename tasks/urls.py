from django.urls import path
from . import views
app_name='tasks'

urlpatterns = [
    path('',views.home,name='home'),
    path('listdetail/<str:id>/',views.createtask,name='listdetail'),
    path('deletetask/<str:id>/',views.deletetask,name='deletetask'),
    path('updatetask/<str:id>/',views.updatetask,name='updatetask'),
    path('updatelist/<str:id>/',views.updatelist,name='updatelist')

]   