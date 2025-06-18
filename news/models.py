from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название тега')

    def __str__(self):
        return self.name
    
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='news', blank=True, verbose_name='Выбор тегов')

    def __str__(self):
        return self.title
