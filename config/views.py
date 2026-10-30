from django.shortcuts import render

# En home(request) fue una vista basada en funciones (FBV), en request: contiene información de la
# solicitud del navegador.
def home(request):
    # En la función return() devuelve la respuesta del usuario.
    return render (request, "home.html")