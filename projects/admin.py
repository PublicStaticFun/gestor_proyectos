from django.contrib import admin
from .models import Project
from tasks.models import Task

class TaskInLine(admin.TabularInline):
    model = Task
    extra = 1
    fields = (
        "title",
        "priority",
        "status",
        "due_date",
        "assigned_to"
    )
    show_change_link = True

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (TaskInLine, )

    list_display = (
        "id",
        "name",
        "status",
        "owner",
        "created_at",
    )

    list_display_links = (
        "id",
        "name"
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "description",
        "owner__username",
    )

    ordering = ("-created_at",)

    date_hierarchy = "created_at"

    list_per_page = 20

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Información del proyecto", {
            "fields": (
                "name",
                "description",
                "status",
                "owner"
            )
        }),
        ("Fechas", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )