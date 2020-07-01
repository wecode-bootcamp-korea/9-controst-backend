from django.contrib import admin
from django.urls import (
    path,
    include
)

urlpatterns = [
   path('partner', include('partner.urls')),
   path('user/', include('user.urls'))
]
