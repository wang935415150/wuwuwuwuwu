from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def server(request):
    print(request.POST)
    return HttpResponse('已收到')
