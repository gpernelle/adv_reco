from django.shortcuts import render
from .models import Adventure
from django.views import generic
from django.db.models import Count


# Create your views here.
def adventure_list(request):
    adventures = Adventure.objects.all()
    return render(request, 'adventure_list.html', {'adventures': adventures})


class AdventureDetailView(generic.DetailView):
    model = Adventure

    def get_object(self):
        """Record the user as having viewed this adventure."""
        obj = super().get_object()
        if self.request.user.is_authenticated:
            obj.viewers.add(self.request.user)
        return obj


class RecommendedAdventuresView(generic.ListView):
    model = Adventure
    template_name = 'adventures/recommended_adventures.html'

    def get_queryset(self):
        """Get adventures from the category that the user has viewed most often."""
        most_viewed_category = self.request.user.viewed_adventures.values('category') \
            .annotate(category_count=Count('category')) \
            .order_by('-category_count') \
            .first()

        if most_viewed_category:
            return Adventure.objects.filter(category=most_viewed_category['category'])
        else:
            return Adventure.objects.none()