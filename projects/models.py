from django.db import models
from django.conf import settings

class Project(models.Model):
    class Status(models.TextChoices):
        PLANNING = "planning", "Planificación"
        ACTIVE = "active", "Activo"
        COMPLETED = "completed", "Completado"
        ON_HOLD = "on_hold", "En pausa"

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PLANNING,
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.name