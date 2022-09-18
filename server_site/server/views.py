from django.forms import model_to_dict
from django.http import HttpResponseBadRequest, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from server.models import Orders


def index(request):
    return HttpResponse('<h1>Main page</h1>')


class OrdersAPIView(APIView):
    def get(self, request):
        data = list(Orders.objects.values())
        return Response(data)


class OrderAPIView(APIView):
    def get(self, request):
        value = request.GET['order_id']
        if Orders.objects.filter(pk=value).exists():
            data = model_to_dict(Orders.objects.get(pk=value))
            return Response(data)
        return HttpResponseBadRequest()

    def post(self, request):
        data = request.data
        print(data)
        if 'user_id' in data and 'order_info' in data and data['user_id'] == 1:
            Orders.objects.create(**data)
            status = 1
        else:
            status = 0
        return Response({"status": status})