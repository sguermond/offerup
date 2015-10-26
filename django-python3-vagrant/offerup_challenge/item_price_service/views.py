from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from django.db.models import Count
from item_price_service.models import ItempricesItemsale

def get_item(request):
    item_q = request.GET.get('item')
    city_q = request.GET.get('city')
    if city_q is None and item_q is not None:
        city_q = "Not specified"
        query = ItempricesItemsale.objects.filter(title=item_q)
        item_count = len(query)
        query = query.values("list_price").annotate(count = Count("list_price")).latest('count')
        price_suggestion = query["list_price"]
        data = {
                "status": 200,
                "content": {
                            "item": item_q,
                            "item_count": item_count,
                            "price_suggestion": price_suggestion,
                            "city": city_q
                 }
                }
    elif city_q is not None and item_q is not None:
        query = ItempricesItemsale.objects.filter(title=item_q, city=city_q)
        item_count = len(query)
        query = query.values("list_price").annotate(count = Count("list_price")).latest('count')
        price_suggestion = query["list_price"]
        data = {
                "status": 200,
                "content": {
                            "item": item_q,
                            "item_count": item_count,
                            "price_suggestion": price_suggestion,
                            "city": city_q
                 }
                }
        
    else:
        data = {"status": 404, "content": {"message": "Not found"}}
    return HttpResponse(json.dumps(data), content_type='application/json')
