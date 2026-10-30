from django.contrib import admin
from django.urls import path, include
from config.views import home

urlpatterns = [
    # Función path() define una ruta y su destino.
    # El admin.site.urls conecta el panel administrativo de Django.
    path('admin/', admin.site.urls),

    # Pagina principal
    # El name="home" asigna un nombre a la ruta para poder referenciarla.
    path("", home, name="home"),

    # Aplicaciones
    path("projects/", include("projects.urls")),
    path("tasks/", include("tasks.urls")),
    path("accounts/", include("accounts.urls")),
]
