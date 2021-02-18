from django.db import models
from .utilities import get_timestamp_path

class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Категория')
    
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
    
    def __str__(self):
        return self.title
        
    
    

class Toy(models.Model):
    brand=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    categories=models.ManyToManyField(Category)
    cost1day=models.PositiveIntegerField(default=0)
    image=models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name='Игрушка'
        verbose_name_plural='Игрушки'
    