import json

from django.views import View
from django.http import JsonResponse
#from django.core.paginator import Paginator
from .models import (
       CounselCenter 
)

class MapView(View):
    def get(self, request):
        centers = CounselCenter.objects.all()
        #paginator = Paginator(centers,20)
        #page = request.GET.get('page', 1)
        #location = paginator.page(page)

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
        #paginator = Paginator(locations,20)
        #page = request.GET.get('page',2)
        #print(page)
        #location = paginator.page(page)

        return JsonResponse({"location":locations}, status=200)
