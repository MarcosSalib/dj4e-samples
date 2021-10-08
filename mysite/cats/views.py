from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from cats.models import Breed, Cat

# Create your views here.

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        breeds_count = Breed.objects.all().count()
        cat_list = Cat.objects.all()

        ctx = {'breeds_count': breeds_count, 'cat_list': cat_list}
        return render(request, 'cats/cat_list.html', ctx)


class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        breed_list = Breed.objects.all()
        ctx = {'breed_list': breed_list}
        return render(request, 'cats/breed_list.html', ctx)


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')
