from django.contrib import admin
from .models import Recipe, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Поля, которые будут отображаться в списке
    search_fields = ('name',)  # Поля, по которым будет доступен поиск

# Регистрация модели Category с настройками CategoryAdmin
admin.site.register(Category, CategoryAdmin)

# Класс для настройки отображения рецептов
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'preparation_time', 'author')  # Поля, которые будут отображаться в списке
    list_filter = ('author', 'categories')  # Фильтры сбоку от списка
    search_fields = ('name', 'description', 'steps')  # Поля, по которым будет доступен поиск
    raw_id_fields = ('author',)  # Поля, для которых будет использоваться виджет выбора вместо выпадающего списка
    filter_horizontal = ('categories',)  # Горизонтальный виджет для ManyToMany полей

# Регистрация модели Recipe с настройками RecipeAdmin
admin.site.register(Recipe, RecipeAdmin)