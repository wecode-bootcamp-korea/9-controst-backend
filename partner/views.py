import json

from django.views import View
from django.http import JsonResponse
from django.db.models import Avg

from .models import (
    Counselor,
    Level,
    Theme, 
    CounselorTheme,
    Kind, 
    CounselorKind, 
    Duration, 
    Product
)
from user.models import History
from comment.models import Review

class CounselorListView(View):
    def get(self, request):
        partners_list = []
        partners = Counselor.objects.all()
        for partner in partners:
            stars = partner.history_set.aggregate(Avg('review__score'))
            review_count = Review.objects.filter(history__in=partner.history_set.all()).count()
            prices = Product.objects.filter(level=partner.level)
            prices_list= [price.price for price in prices]
            partners_list.append(
                    {
                        "name"                   : partner.name, 
                        "gender"                 : partner.gender, 
                        "level"                  : partner.level.name, 
                        "counsel_count"          : partner.counsel_count, 
                        "introduction"           : partner.introduction, 
                        "is_cousel_count_gt_150" : partner.is_counsel_count_gt_150, 
                        "profile_image_url"      : partner.profile_image_url, 
                        "prices"                 : prices_list,
                        "stars"                  : stars,
                        "review_count"           : review_count
                     }
                )

        return JsonResponse({"information":partners_list}, status=200)

