from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Объявление
class Ad(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
    )
    description = models.TextField()


    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='ads',  # все объявления в категории будут доступны через поле ads
    )



    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('ad_detail', args=[str(self.id)])

# Категория, к которой будет привязываться объявление
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()

class AdCategory(models.Model):
    postThrough = models.ForeignKey(Ad, on_delete = models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    adComment = models.ForeignKey(Ad, on_delete = models.CASCADE)
    userComment = models.ForeignKey(User, on_delete=models.CASCADE)
    textComment = models.TextField()
