import json

from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from api.models import Test


@require_http_methods(["GET"])
def add_name(request):
    response = {}
    try:
        name = request.GET.get('name')
        age = request.GET.get('age')
        book = Test(name=name, age=age)
        book.save()
        response['respMsg'] = 'success'
        response['respCode'] = '000000'
    except Exception as e:
        response['respMsg'] = str(e)
        response['respCode'] = '999999'
    return JsonResponse(response)


@require_http_methods(["GET"])
def get_name(request):
    response = {}
    try:
        books = Test.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['respMsg'] = 'success'
        response['respCode'] = '000000'

    except Exception as e:
        response['respMsg'] = str(e)
        response['respCode'] = '999999'
    return JsonResponse(response)