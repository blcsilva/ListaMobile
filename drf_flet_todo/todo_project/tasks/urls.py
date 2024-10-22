# todo_project/urls.py

from django.contrib import admin
from django.urls import path, include
from tasks.views import home  # Certifique-se de importar a view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Adicione esta linha
    path('api/', include('todo_app.api.urls')),  # Supondo que você tenha esta configuração
]
