from django.urls import path
from . import views

# Define un espacio de nombres para identificar las rutas de esta aplicación.
app_name = "projects"

urlpatterns = [
    path("", views.project_list, name="list"),
    path(
        # "<int:project_id>/" significa que Django acepta un número entero en esa parte de la ruta
        # y lo pasa a la vista como argumento.
        "<int:project_id>/",
        views.project_detail,
        name="detail",
    ),
]
