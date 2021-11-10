from django.contrib import admin
from .models import Engine, Category

class EngineAdmin(admin.ModelAdmin):    # Страничка на сайте, которая будет отображать
    list_display = ["name", "image" ]   # Свойства которые будут отображаться
    prepopulated_fields = {"slug": ("name",)}     # Втоматическая генерация на основе других значений

admin.site.register(Engine, EngineAdmin)   # Включить отображения "Этого всего" в админку


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", ]
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)