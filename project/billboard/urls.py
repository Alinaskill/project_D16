from django.urls import path
from .views import (
    AdsList, AdDetail, AdCreate, AdUpdate, AdDelete,
)

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем объявлениям у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', AdsList.as_view(), name='ad_list'),
   # pk — это первичный ключ объявления, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:id>', AdDetail.as_view(), name='ad_detail'),
   path('create/', AdCreate.as_view(), name='ad_create'),
   path('<int:pk>/edit/', AdUpdate.as_view(), name='ad_edit'),
   path('<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),
]
