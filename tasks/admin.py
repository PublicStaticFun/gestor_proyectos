from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    actions = ("mark_as_completed",)

    @admin.action(description="Marcar tareas seleccionadas como completadas")
    def mark_as_completed(self, request, queryset):
        updated = queryset.updated(status=Task.Status.COMPLETED)

        self.message_user(
            request,
            f"{updated} tarea(s) marcada(s) como completadas. "
        )

    list_display = (
        "id",
        "title",
        "project",
        "priority",
        "status",
        "assigned_to",
        "due_date",
    )

    list_display_links = ("id", "title")

    list_filter = (
        "status",
        "priority",
        "due_date",
        "project",
    )

    search_fields = (
        "title",
        "description",
        "project__name",
        "assigned_to__username"
    )

    ordering = ("due_date", "-created_at")

    list_per_page = 25

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    autocomplete_fields = (
        "project",
        "assigned_to"
    )

    fieldsets = (
        ("Información de la tarea", {
            "fields": (
                "title",
                "description",
                "project",
            )
        }),
        ("Seguimiento", {
            "fields": (
                "priority",
                "status",
                "due_date",
                "assigned_to",
            )
        }),
        ("Fechas del registro", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )