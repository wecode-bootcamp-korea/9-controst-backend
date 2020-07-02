from django.urls import path, include
from user.views import SignUpView, SignInView, HistoryView

urlpatterns = [
   path('signup', SignUpView.as_view()),
   path('signin', SignInView.as_view()),
   path('history', HistoryView.as_view()),
]
