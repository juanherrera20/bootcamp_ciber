from django.contrib import admin
from .models import Departamento, City, Ubication


class CityInline(admin.TabularInline):
    model = City
    extra = 1


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [CityInline]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "departamento")
    list_filter = ("departamento",)
    search_fields = ("name", "departamento__name")


@admin.register(Ubication)
class UbicationAdmin(admin.ModelAdmin):
    list_display = ("address", "city", "latitude", "longitude", "postal_code")
    list_filter = ("city", "city__departamento")
    search_fields = (
        "address",
        "city__name",
        "city__departamento__name",
        "postal_code",
    )
    fieldsets = [
        ("Información Básica", {"fields": ("address", "city", "postal_code")}),
        ("Geolocalización", {"fields": ("latitude", "longitude")}),
        ("Notas", {"fields": ("notes",)}),
    ]
