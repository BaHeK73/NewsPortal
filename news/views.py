from django.views.generic import TemplateView, ListView, DetailView
from .models import News

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = "03.06.2025"
        return context

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news'

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'

class AboutView(TemplateView):
    template_name = 'about.html'
