from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('addtask/',views.addtask),
    path('edittask/',views.edittask,name = 'edittask'),
    path('<int:pk>',views.TaskDetailView.as_view(),name = 'task_detail'),
    path('<int:pk>/update',views.TaskUpdateView.as_view(),name = 'task_update'),
    path('<int:pk>/delete',views.TaskDeleteView.as_view(),name = 'task_delete'),
    path('create/',views.create),
]