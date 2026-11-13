from django.contrib import admin
from django.urls import include, path
from gestion_bibliotheque import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.LivreListView.as_view(), name="livre_list"),
    path("livres/ajouter/", views.LivreCreateView.as_view(), name="livre_create"),
    path("livres/<int:pk>/", views.LivreDetailView.as_view(), name="livre_detail"),
    path("livres/<int:pk>/modifier/", views.LivreUpdateView.as_view(), name="livre_update"),
    path("livres/<int:pk>/supprimer/", views.LivreDeleteView.as_view(), name="livre_delete"),
    path("livres/<int:pk>/disponibilite/", views.basculer_disponibilite, name="livre_toggle"),
]
