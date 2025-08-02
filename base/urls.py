from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login-page"),

    path("logout/", views.logout_page, name="logout-page"),

    path("", views.task_list, name='task-list'),

    path("create-task/", views.create_task, name="create-task"),

    path("update-task/<str:pk>/", views.update_task, name="update-task"),   #pk = primary key

    path("delete-task/<str:pk>/", views.delete_task, name="delete-task"),

    path("toggle-task/<int:pk>/", views.toggle_task, name="toggle-task"),

]



# username - admin, password - Django@123 