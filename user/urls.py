from django.urls import path, include
from user.views import (
        SignUpView,
        SignInView,
        EmailCheckView,
        NicknameCheckView,
        HistoryView,
)

urlpatterns = [
   path('/signup', SignUpView.as_view()),
   path('/signin', SignInView.as_view()),
   path('/emailcheck', EmailCheckView.as_view()),
   path('/nickcheck', NicknameCheckView.as_view()),
   path('/history', HistoryView.as_view()),
]


