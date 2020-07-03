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
    Product,
    CounselorContent
)
from user.models import History
from comment.models import Review

class CounselorListView(View):
    def get(self, request):
        partners_list = []
        offset        = request.GET.get('offset', 1)
        limit         = request.GET.get('limit', 12)
        partners = Counselor.objects.prefetch_related('history_set').prefetch_related('history_set__review_set')[offset:limit]
        reviews  = Review.objects.select_related('history').all()
        products = Product.objects.select_related('level').all()
        for partner in partners:
            stars        = partner.history_set.aggregate(Avg('review__score'))
            review_count = reviews.filter(history__in=partner.history_set.all()).count()
            prices  = [price.price for price in products.filter(level=partner.level)]
            partners_list.append(
                    {
                        "partner_id"             : partner.id,
                        "name"                   : partner.name, 
                        "gender"                 : partner.gender, 
                        "level"                  : partner.level.name, 
                        "counsel_count"          : partner.counsel_count, 
                        "introduction"           : partner.introduction, 
                        "is_cousel_count_gt_150" : partner.is_counsel_count_gt_150, 
                        "profile_image_url"      : partner.profile_image_url, 
                        "prices"                 : prices,
                        "stars"                  : stars,
                        "review_count"           : review_count
                     }
                )

        return JsonResponse({"information":partners_list}, status=200)

class CounselorDetailView(View):
     def get(self, request, partner_id):
         partner_detail = []

         partner      = Counselor.objects.get(id=partner_id)
         prices       = Product.objects.filter(level=partner.level)
         prices_list  = [price.price for price in prices]
         stars        = partner.history_set.aggregate(Avg('review__score'))
         review_count = Review.objects.filter(history__in=partner.history_set.all()).count()
         partner_detail.append(
                 {
                     "partner_name"           : partner.name,
                     "partner_level"          : partner.level.name,
                     "counsel_count"          : partner.counsel_count,
                     "is_cousel_count_gt_150" : partner.is_counsel_count_gt_150,
                     "profile_image_url"      : partner.profile_image_url,
                     "prices"                 : prices_list,
                     "stars"                  : stars,
                     "review_count"           : review_count,

                 }
          )

         content = CounselorContent.objects.get(counselor=partner_id).name
         partner_detail.append(
                 {
                     "patner_content" : eval(content)
                 }
             )

         counselor_histories = Counselor.objects.prefetch_related('history_set').get(id=partner_id).history_set.all()
         counselor_reviews   = Review.objects.filter(history__in=counselor_histories)
         reviews_list        = [
                 {
                     'review_created' : i.created_at,
                     'review_score'   : i.score,
                     'review_comment' : i.comment
                 } for review in counselor_reviews
            ]

         partner_detail.append(
                 {
                 "reviews" : reviews_list
                 }
          )
         return JsonResponse({"information":partner_detail}, status=200)
