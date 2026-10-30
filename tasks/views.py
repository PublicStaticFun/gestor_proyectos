from django.shortcuts import render
from django.http import HttpResponse

def task_list(request):
    return render (
        request,
        "tasks/task_list.html",
        {"tasks": []},
    )

def task_detail(request, task_id):
    return HttpResponse(
        f"<h1>Tarea {task_id}</h1>"
        "<p>El detalle se conectara a la base de datos </p>"
        "<p>en los siguientes pasos.</p>"
    )