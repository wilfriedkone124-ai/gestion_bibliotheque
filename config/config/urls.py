"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
        path("", views.LivreListView.as_view(), name="livre_list"),
    path("livres/ajouter/", views.LivreCreateView.as_view(), name="livre_create"),
    path("livres/<int:pk>/", views.LivreDetailView.as_view(), name="livre_detail"),
    path("livres/<int:pk>/modifier/", views.LivreUpdateView.as_view(), name="livre_update"),
    path("livres/<int:pk>/supprimer/", views.LivreDeleteView.as_view(), name="livre_delete"),
    path("livres/<int:pk>/disponibilite/", views.basculer_disponibilite, name="livre_toggle"),
]
