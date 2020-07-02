import json

from django.views import View
from django.http import JsonResponse

from .models import (
       CounselCenter 
)

class MapView(View):
    def get(self, request):
        locations = []
        centers = CounselCenter.objects.all()
        for center in centers:
            locations.append(
                {
                    "mapX"                 : center.longitude,
                    "mapY"                 : center.latitude,
                    "type"                 : center.center_type,
                    "title"                : center.name,
                    "link"                 : center.homepage_url,
                    "telephone"            : center.phone_number,
                    "address"              : center.address,
                    "roadAddress"          : center.road_address,
                    "isTrostPartnerCenter" : center.is_trost_partner,
                    "trostPartners"        : eval(center.partner_info),
                    "counselingTypes"      : eval(center.counseling_type)
                    }
        )

        return JsonResponse({"location":locations}, status=200)
