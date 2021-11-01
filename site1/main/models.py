from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)       # Строка с симфолами, для названий
    slug = models.SlugField(max_length=200, db_index=True, unique=True)   # Ссылка на категорию транслитом
    image = models.ImageField(upload_to="Engins")                # ИСПРАВИТЬ | Изображения которые которые хратьнсятся в папке
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children", on_delete=models.CASCADE)     # Связь с другими таблицаи из базы | Связываем ключь одной таблицы с другой таблицей
    class Meta:        # Подкласс для оформления(вспомогательный класс), Сортировка
        ordering =("name",)
        verbose_name ="Категория"
        verbose_name_plural = "Категории"
        unique_together =("slug", "parent",)

    def get_absolute_url(self):
        return reverse("main:product_list_by_category", args=[self.slug])



class Engine(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    power = models.PositiveIntegerField()         # Положительное целове число
    image = models.ImageField(upload_to="Engins")
    slug = models.SlugField(max_length=200, db_index=True)
    category = models.ForeignKey(Category, blank=True, null=True, related_name="product", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    product_information = models.TextField(blank=True)
    stock = models.PositiveIntegerField()          # Колличество на складе
    availbale = models.BooleanField(default=True)     # Логическтое поле
    created = models.DateField(auto_now_add=True)     # Поля с датой и временем, когда был товар создан
    updated = models.DateField(auto_now=True)     # Когда был товар отредактирован

    def get_absolute_url(self):
        return reverse("main:product_detail", args=[self.id, self.slug])
