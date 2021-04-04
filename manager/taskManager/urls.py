from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.tasks, name="task-manager"),
    # path('account/', include('account.urls'))
]