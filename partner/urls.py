from django.urls import path
from .views import ListUp

urlpatterns = [
        path('', ListUp.as_view()),
        ]
