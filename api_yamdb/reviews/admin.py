from django.contrib import admin

from .models import Category, Genre, Title


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Настройки для категорий. """

    list_display = ('name', 'slug',)
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Настройки жанров."""

    list_display = ('name', 'slug',)
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    """Настройки произведений."""

    list_display = ('name', 'year', 'category', 'description',)
    list_filter = ('name',)
    search_fields = ('name', 'year', 'category',)
    empty_value_display = '-пусто-'
