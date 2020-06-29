'''
import json

from django.views import View
from django.http import JsonResponse

from .models import Counselor, Level, Theme, CounselorTheme, Kind, CounselorKind, Duration, Product

class ListUp(View):
    def get(self, request):
        n = 1
        for i in range(56):
           counselor =  Counselor.objects.get(id=n)
            n += 1
        partners = [
                {name: counselor.name, gender:gender, level:level, counsel_count:counsel_count, introduction:introduction, is_counsel_count_gt_150:is_counsel_count_gt_150, profile_image_url:profile_image_url}, {}
                ]
        return JsonResponse({"information":partners}, status=200)
'''
