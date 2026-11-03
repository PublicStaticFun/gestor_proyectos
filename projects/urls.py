from django.urls import path
from . import views

# Define un espacio de nombres para identificar las rutas de esta aplicación.
app_name = "projects"

urlpatterns = [
    path("", views.project_list, name="project_list"),
    path("crear/", views.project_create, name="project_create"),
    path("<int:project_id>/", views.project_detail, name="project_detail"),
    path(
        "<int:project_id>/editar/",
        views.project_update,
        name="project_update",
    ),
    path(
        "<int:project_id>/eliminar/",
        views.project_delete,
        name="project_delete"
    ),
]
