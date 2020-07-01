import json

from django.views import View
from django.http import JsonResponse

from .models import (
       CounselCenter 
)

class MapView(View):
    def get(self, request):
        location = []
        centers = CounselCenter.objects.all()
        for center in centers:
            location.append(
                {
                    "mapX": center.longitude,
                    "mapY": center.latitude,
                    "type": center.center_type,
                    "title": center.name,
                    "link": center.homepage_url,
                    "telephone": center.phone_number,
                    "address": center.address,
                    "roadAddress": center.road_address,
                    "isTrostPartnerCenter": center.is_trost_partner,
                    "trostPartners": center.partner_info,
                    "counselingTypes": center.counseling_type
                    }
)


        return JsonResponse({"location":location}, status=200)
# Create your views here.
