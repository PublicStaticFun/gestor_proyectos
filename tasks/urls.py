from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("crear/", views.task_create, name="task_create"),
    path("<int:task_id>", views.task_detail, name="task_detail"),
    path(
        "<int:task_id>/editar/",
        views.task_update,
        name="task_update",
    ),
    path(
        "<int:task_id>/eliminar/",
        views.task_delete,
        name="task_delete",
    ),
]
