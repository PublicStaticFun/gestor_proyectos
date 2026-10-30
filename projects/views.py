from django.shortcuts import render
from django.http import HttpResponse

# Se han creado dos vistas: project_list y project_detail
# En project_list se mostrara el listado de proyectos.
def project_list(request):
    context = {
        "projects": [],
    }
    return render (
        request,
        "projects/project_list.html",
        context,
    )

# En project_detail se mostrara un proyecto especifico.
# Se observa un parametro project_id: que nos permitirá identificar un proyecto mediante su número
# en la URL.
def project_detail(request, project_id):
    return HttpResponse (
        f"<h1>Proyecto {project_id}</h1>"
        "<p>El detalle se conectara a la base de datos </p>"
        "<p>en los siguientes pasos.</p>"
    )