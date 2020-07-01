from django.urls import path
from .views import (
        CounselorListView,
        )

urlpatterns = [
    path('', CounselorListView.as_view()),
]
