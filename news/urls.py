from django.urls import path
from .views import HomeView, NewsListView, NewsDetailView, AboutView, ArticleListView, ArticleDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
] 