from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from django.contrib.auth.mixins import PermissionRequiredMixin

from .filters import AdFilter
from .forms import AdForm
from .models import Ad


class AdsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Ad
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'name'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'ads.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'ads'
    paginate_by = 10  # вот так мы можем указать количество записей на странице

    # Переопределяем функцию получения списка объявлений
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = AdFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список объявлений
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context



class AdDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному объявлению
    model = Ad
    # Используем другой шаблон — ad.html
    template_name = 'ad.html'
    # Название объекта, в котором будет выбранное пользователем объявление
    context_object_name = 'ad'
    pk_url_kwarg = 'id'


# Добавляем новое представление для создания объявлений.
class AdCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = AdForm
    # модель
    model = Ad
    # и новый шаблон, в котором используется форма.
    template_name = 'ad_edit.html'


class AdUpdate(UpdateView):
    form_class = AdForm
    model = Ad
    template_name = 'ad_edit.html'

class AdDelete(DeleteView):
    model = Ad
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('ad_list')

#Предоставление прав

class MyCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('billboard.add_ad')

class MyUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('billboard.change_ad')





