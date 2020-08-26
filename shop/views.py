from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):

    return render(request,"shop/index.html")


def about (request):
    return HttpResponse("WE R AT contact")
    # return render(request,"shop/index.html")

def contact (request):
    return HttpResponse("WE R AT contact")
    # return render(request,"shop/index.html")
def tracker (request):
    return HttpResponse("WE R AT tracker ")
    # return render(request,"shop/index.html")
def search (request):
    return HttpResponse("WE R AT search")
    # return render(request,"shop/index.html")
def prodview (request):
    return HttpResponse("WE R AT prodview")
    # return render(request,"shop/index.html")
def checkout (request):
    return HttpResponse("WE R AT checkout ")
    # return render(request,"shop/index.html")