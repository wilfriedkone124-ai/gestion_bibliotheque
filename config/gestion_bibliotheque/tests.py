from django.test import TestCase
from django.urls import reverse

from .models import Categorie, Livre


class LivreViewsTests(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(nom="Roman")

    def test_catalogue_is_displayed(self):
        response = self.client.get(reverse("livre_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Catalogue des livres")

    def test_livre_can_be_created(self):
        response = self.client.post(
            reverse("livre_create"),
            {
                "titre": "Le livre",
                "auteur": "Auteur",
                "categorie": self.categorie.pk,
                "disponible": "on",
            },
        )

        self.assertRedirects(response, reverse("livre_list"))
        self.assertTrue(Livre.objects.filter(titre="Le livre", auteur="Auteur").exists())

    def test_availability_can_only_be_toggled_with_post(self):
        livre = Livre.objects.create(
            titre="Le livre",
            auteur="Auteur",
            categorie=self.categorie,
        )
        url = reverse("livre_toggle", args=[livre.pk])

        self.assertEqual(self.client.get(url).status_code, 405)
        response = self.client.post(url)

        self.assertRedirects(response, reverse("livre_detail", args=[livre.pk]))
        livre.refresh_from_db()
        self.assertFalse(livre.disponible)
