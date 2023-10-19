from django.http import HttpResponse
from django.shortcuts import render
from . models import place, Meet

# Create your views here.

def demo(request):
    obj = place.objects.all()
    obj1 = Meet.objects.all()
    return render(request, "index.html", {'result': obj, 'result2': obj1})

#
# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res = x+y
#     return render(request, "result.html", {'result': res})
