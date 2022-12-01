from .models import Category, Ad
from django.contrib import admin

# создаём новый класс для представления новостей в админке
class AdAdmin(admin.ModelAdmin):
    # list_display - это список или кортеж со всеми полями, которые вы хотите видеть в таблице с объявлениями
    list_display = ('name', 'category')
    list_filter = ('name', 'category')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('name', 'category')  # тут всё очень похоже на фильтры из запросов в базу


admin.site.register(Category)
admin.site.register(Ad, AdAdmin)

