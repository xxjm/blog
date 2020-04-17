
from django.urls import path, include
from . import views

app_name="todolist"
urlpatterns = [
    path('bianji/<i_id>', views.bianji,name="编辑"),
    path('edit/', views.edit,name="项目"),
    path('del/<i_id>', views.delete, name="删除"),
    path('bianji/', views.bianji,name="编辑"),
    path('cross/<i_id>', views.cross, name='划掉')
]
