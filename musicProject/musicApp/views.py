from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# function that prints the HTTRESPONSE when called
def index(request):
    return HttpResponse("use this paths to find out more about these artist 'kendricklamar/', 'dannybrown/', 'chancetherapper'")


def kendrick(request):
    return HttpResponse("Kendrick Lamar is the greatest rapper alive")


def danny(request):
    return HttpResponse("danny Brown music is funny")


def chance(request):
    return HttpResponse("chance makes great music")