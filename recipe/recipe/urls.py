
from django.contrib import admin
from django.urls import path, include  # Импортируем функцию include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')), 
    path('__debug__/', include("debug_toolbar.urls")),
]