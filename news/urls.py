from django.urls import path
from .views import HomeView, NewsListView, NewsDetailView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('about/', AboutView.as_view(), name='about'),
] 