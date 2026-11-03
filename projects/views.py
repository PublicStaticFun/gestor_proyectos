from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Project
from .forms import ProjectForm

@login_required
def project_list(request):
    projects = Project.objects.filter(
        owner = request.user
    )
    return render(
        request,
        "projects/project_list.html",
        {"projects": projects},
    )

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(
        Project,
        pk=project_id,
        owner=request.user
    )
    return render (
        request,
        "projects/project_detail.html",
        {"project": project},
    )

@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()

            messages.success(request, "Proyecto creado recientemente.")
            return redirect("projects:project_detail", project_id = project.pk)
        else:
            form = ProjectForm()

        return render(
            request,
            "projects/project_form.html",
            {"form": form, "title": "Crear proyecto"},
        )

    else:
        form = ProjectForm()

        return render(
            request,
            "projects/project_form.html",
            {"form": form, "title": "Crear proyecto"},
        )

@login_required
def project_update(request, project_id):
    project = get_object_or_404(
        Project,
        pk=project_id,
        owner=request.user,
    )

    if request.method == "POST":
        form = ProjectForm(
            request.POST,
            instance=project,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Proyecto actualizado correctamente."
            )

            return redirect(
                "projects:project_detail",
                project_id=project.pk,
            )
    else:
        form = ProjectForm(instance=project)

    return render(
        request,
        "projects/project_form.html",
        {
            "form": form,
            "title": "Editar proyecto",
        },
    )

@login_required
def project_delete(request, project_id):
    project = get_object_or_404(
        Project,
        pk=project_id,
        owner=request.user,
    )

    if request.method == "POST":
        project.delete()
        messages.success(request, "Proyecto eliminado recientemente")
        return redirect("projects:project_list")

    return render(
        request,
        "projects/project_confirm_delete.html",
        {"project": project},
    )