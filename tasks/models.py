from django.db import models
from django.conf import settings

class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = "low", "Bajo"
        MEDIUM = "medio", "Medio"
        HIGH = "high", "Alto"
        URGENT = "urgent", "Urgente"

    class Status(models.TextChoices):
        TODO = "todo", "Pendiente"
        IN_PROGRESS = "in_progress", "En progreso"
        COMPLETED = "completed", "Completado"

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )

    due_date = models.DateField(
        null=True,
        blank=True,
    )

    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tasks",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["due_date", "-created_at"]
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        return self.title