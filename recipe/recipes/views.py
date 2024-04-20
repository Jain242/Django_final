from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Category
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Главная страница с рецептами
def home(request):
    recipes = Recipe.objects.order_by('?')[:5]  # Получаем 5 случайных рецептов
    return render(request, 'home.html', {'recipes': recipes})

# Страница с детальным описанием рецепта
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

# Добавление нового рецепта
@login_required
def recipe_add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})