from django.contrib import admin
from .models import Categorie, Livre
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ("nom", "nombre_livres")
    search_fields = ("nom",)
    @admin.display(description="Nombre de livres")
    def nombre_livres(self, obj):
        return obj.livres.count()
@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ("titre", "auteur", "categorie", "disponible", "date_ajout")
    list_filter = ("categorie", "disponible")
    list_editable = ("disponible",)
    search_fields = ("titre", "auteur")