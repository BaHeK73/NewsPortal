from django.views.generic import TemplateView, ListView, DetailView
from .models import News, Tag
from django.db.models import Q
from datetime import datetime

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.now().strftime('%d.%m.%Y')
        return context

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.request.GET.get('tag')
        order = self.request.GET.get('order')
        q = self.request.GET.get('q')
        if tag_id and tag_id.isdigit():
            queryset = queryset.filter(tags__id=tag_id)
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(content__icontains=q)
            )
        if order == 'asc':
            queryset = queryset.order_by('created_at')
        else:
            queryset = queryset.order_by('-created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['selected_tag'] = self.request.GET.get('tag', '')
        context['order'] = self.request.GET.get('order', 'desc')
        context['q'] = self.request.GET.get('q', '')
        return context

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'

class AboutView(TemplateView):
    template_name = 'about.html'

