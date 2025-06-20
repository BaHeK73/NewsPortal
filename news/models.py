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
    

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, verbose_name="Название сайта")
    logo = models.ImageField(upload_to="logo/", verbose_name="Логотип", blank=True)

    def clean(self) -> None:
        if not self.pk and SiteSettings.objects.exists():
            return ValidationError("Больше нельзя")

    def __str__(self) -> str:
        return "Настройеи сайта"
    
    class Meta:
        verbose_name = "Настройеи сайта"

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок статьи')
    content = models.TextField(verbose_name='Содержимое статьи')
    image = models.ImageField(upload_to='article_images/', null=True, blank=True, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title
