from django.shortcuts import render, get_object_or_404
from .models import Project

# Se han creado dos vistas: project_list y project_detail
# En project_list se mostrara el listado de proyectos.
def project_list(request):
    projects = Project.objects.all()

    return render (
        request,
        "projects/project_list.html",
        {"projects": projects},
    )

# En project_detail se mostrara un proyecto especifico.
# Se observa un parametro project_id: que nos permitirá identificar un proyecto mediante su número
# en la URL.
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render (
        request,
        "projects/project_detail.html",
        {"project": project},
    )