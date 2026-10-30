from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Task

def task_list(request):
    tasks = Task.objects.select_related(
        "project",
        "assigned_to",
    )

    return render (
        request,
        "tasks/task_list.html",
        {"tasks": tasks},
    )

def task_detail(request, task_id):
    task = get_object_or_404(
        Task.objects.select_related("project", "related_to"),
        pk=task_id,
    )
    return render(
        request,
        "tasks/task_detail.html",
        {"task": task},
    )