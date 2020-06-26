import json

from django.views import View
from django.http import(
        JsonResponse,
        HttpResponse
        )

from .models import Counselor, Level, Theme, CounselorTheme, Kind, CounselorKind, Duration, Product

class Partner(View):
    def get(self, request):
        partner_list = [
                {'name':
                 'img':
                 'level':
                 'introduction':
                 }
                
                ]
        return JsonResponse
