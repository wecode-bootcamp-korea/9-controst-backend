import json

from django.views import View
from django.http import JsonResponse

from .models import Counselor, Level, Theme, CounselorTheme, Kind, CounselorKind, Duration, Product

class ListUp(View):
    def get(self, request):
        partners_list = []
        partners = Counselor.objects.all()
        products = Product.objects.all()
        for partner in partners:
            prices_list = []
            prices = Product.objects.filter(level=partner.level)
            for price in prices:
                prices_list.append(price.price)
            partners_list.append({"name":partner.name, "gender":partner.gender, "level":partner.level.name, "counsel_count":partner.counsel_count, "introduction":partner.introduction, "is_cousel_count_gt_150":partner.is_counsel_count_gt_150, "profile_image_url":partner.profile_image_url, "prices":prices_list})


        return JsonResponse({"information":partners_list}, status=200)
