import json

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from server.models import Orders


def index(request):
    return render(request, 'server/index.html')


def get_all_orders(request):
    data = list(Orders.objects.values())
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def get_order(request):
    if request.method == 'GET':
        value = request.GET['order_id']
        try:
            value = int(value)
        except:
            return HttpResponseBadRequest()
        if Orders.objects.filter(pk=value).exists():
            data = list(Orders.objects.filter(pk=value).values())
            return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

        return HttpResponseBadRequest()

    if request.method == 'POST':
        data = json.loads(request.body.decode())
        if 'user_id' in data and 'order_info' in data and data['user_id'] == '1':
            Orders.objects.create(**data)
            status = 1
        else:
            status = 0

        data = {"status": status}
        return JsonResponse(data, safe=False)

