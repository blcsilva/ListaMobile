from django.contrib import admin  # Importação correta do admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet  # Ajuste o import para seu app de tarefas

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),  # O erro estava aqui, faltava importar o admin
    path('api/', include(router.urls)),
]
