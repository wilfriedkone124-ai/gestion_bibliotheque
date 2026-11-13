from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import LivreForm
from .models import Categorie, Livre
class LivreListView(ListView):
    model = Livre
    template_name = "bibliotheque/livre_list.html"
    context_object_name = "livres"
    paginate_by = 10
    def get_queryset(self):
        qs = Livre.objects.select_related("categorie")
        categorie = self.request.GET.get("categorie", "")
        if categorie.isdigit():
            qs = qs.filter(categorie_id=int(categorie))
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(Q(titre__icontains=q) | Q(auteur__icontains=q))
        return qs
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        params = self.request.GET.copy()
        params.pop("page", None)
        ctx["categories"] = Categorie.objects.all()
        ctx["categorie_active"] = self.request.GET.get("categorie", "")
        ctx["q"] = self.request.GET.get("q", "")
        ctx["querystring"] = params.urlencode()
        return ctx
class LivreDetailView(DetailView):
    model = Livre
    template_name = "bibliotheque/livre_detail.html"
class LivreCreateView(CreateView):
    model = Livre
        form_class = LivreForm
    template_name = "bibliotheque/livre_form.html"
    success_url = reverse_lazy("livre_list")
    def form_valid(self, form):
        messages.success(self.request, "Le livre a été ajouté.")
        return super().form_valid(form)
class LivreUpdateView(UpdateView):
    model = Livre
    form_class = LivreForm
    template_name = "bibliotheque/livre_form.html"
    success_url = reverse_lazy("livre_list")
    def form_valid(self, form):
        messages.success(self.request, "Le livre a été modifié.")
        return super().form_valid(form)
class LivreDeleteView(DeleteView):
    model = Livre
    template_name = "bibliotheque/livre_confirm_delete.html"
    success_url = reverse_lazy("livre_list")
    def form_valid(self, form):
        messages.success(self.request, "Le livre a été supprimé.")
        return super().form_valid(form)
@require_POST
def basculer_disponibilite(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    livre.disponible = not livre.disponible
    livre.save(update_fields=["disponible"])
    messages.info(request, "Disponibilité mise à jour.")
    return redirect("livre_detail", pk=livre.pk)