from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden

from projects.models import Project
from .models import Task
from .forms import TaskForm

User = get_user_model()

@login_required
def task_list(request):
    tasks = Task.objects.filter(
        project__owner = request.user
    ).select_related("project", "assigned_to")

    return render(
        request,
        "tasks/task_list.html",
        {"tasks": tasks},
    )

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(
        Task.objects.select_related("project", "assigned_to"),
        pk=task_id,
        project__owner = request.user,
    )

    return render(
        request,
        "tasks/task_detail.html",
        {"task": task},
    )

@login_required
def task_create(request):
    projects = Project.objects.filter(owner=request.user)

    if not projects.exists():
        messages.warning(
            request,
            "Primero debes crear un proyecto para añadir tareas.",
        )
        return redirect("projects:project_create")

    if request.method == "POST":
        form = TaskForm(request.POST)
        form.fields["project"].queryset = projects
        form.fields["assigned_to"].queryset = User.objects.filter(
            pk=request.user.pk
        )

        if form.is_valid():
            task = form.save()
            messages.success(request, "Tarea creada correctamente")
            return redirect("tasks:task_detail", task_id=task.pk)
    else:
        form = TaskForm()
        form.fields["project"].queryset = projects
        form.fields["assigned_to"].queryset = User.objects.filter(
            pk=request.user.pk
        )

        project_id = request.GET.get("project")
        if project_id:
            form.fields["project"].initial = project_id

    return render(
        request,
        "tasks/task_form.html",
        {"form": form, "title": "Crear tarea"}
    )

@login_required
def task_update(request, task_id):
    task = get_object_or_404(
        Task,
        pk=task_id,
        project__owner = request.user,
    )

    projects = Project.objects.filter(owner = request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
    else:
        form = TaskForm(instance=task)

    form.fields["project"].queryset = projects
    form.fields["assigned_to"].queryset = User.objects.filter(
        pk = request.user.pk
    )

    if request.method == "POST" and form.is_valid():
        updated_task = form.save()
        messages.success(request, "Tarea actualizada correctamente. ")
        return redirect(
            "tasks:task_detail",
            task_id = updated_task.pk,
        )
    return render(
        request,
        "tasks/task_form.html",
        {"form": form, "title": "Editar tarea"},
    )

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(
        Task,
        pk=task_id,
        project__owner = request.user,
    )

    if request.method == "POST":
        task.delete()
        messages.success(request, "Tarea eliminada correctamente. ")
        return redirect("tasks:task_list")

    return render(
        request,
        "tasks/task_confirm_delete.html",
        {"task": task},
    )