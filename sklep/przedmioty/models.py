
from django.db import models

from glowny.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default='')  # Poprawienie literówki w polu 'description'.
    parent_category = models.ForeignKey('self', related_name='subcategories', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)  # Określenie domyślnego porządku sortowania kategorii.
        verbose_name_plural = 'Categories'  # Nadanie nazwy w liczbie mnogiej w panelu admina.

    def __str__(self):
        return self.name  # Zwraca nazwę kategorii jako jej reprezentację w tekście.


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    min_price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name  # Zwraca nazwę przedmiotu jako jego reprezentację w tekście.
