from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('account/', include('account.urls')),
    path('task-manager/', include('taskManager.urls')),
    path('password-manager/', include('passwordManager.urls')),
]
