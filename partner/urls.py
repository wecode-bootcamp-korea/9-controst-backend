from django.urls import path
from .views import (
        CounselorListView,
        CounselorDetailView
        )

urlpatterns = [
    path('', CounselorListView.as_view()),
    path('/<slug:partner_id>', CounselorDetailView.as_view())
]


