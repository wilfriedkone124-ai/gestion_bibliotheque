from django.db import models
from django.urls import reverse
class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    class Meta:
        ordering = ["nom"]
        verbose_name = "catégorie"
        verbose_name_plural = "catégories"
    def __str__(self):
        return self.nom
class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=150)
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT, related_name="livres")
    disponible = models.BooleanField(default=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["titre"]
        constraints = [
            models.UniqueConstraint(
                fields=["titre", "auteur"],
                name="livre_unique_titre_auteur",
                violation_error_message="Ce livre existe déjà pour cet auteur.",
            )
        ]
    def __str__(self):
        return f"{self.titre} - {self.auteur}"
    def get_absolute_url(self):
        return reverse("livre_detail", args=[self.pk])