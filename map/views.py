import json

from django.views import View
from django.http import JsonResponse
from .models import (
       CounselCenter 
)

class MapView(View):
    def get(self, request):
        page    = request.GET.get('page', 1)
        limit   = 20*int(page)
        offset  = limit-20
        centers = CounselCenter.objects.all()[offset:limit]

        locations = [ 
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
                for center in centers
        ]

        return JsonResponse({"location":locations}, status=200)
