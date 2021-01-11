from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'sampleApp/home.html')


def passView(request):

    thePassword = ''

    lowerCase = list('abcdefghijklmnopqrstuvwxyz')
    uperCase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    number = list('01928870649')
    specialChar = list('!@#$%^&*<>?')

    # length = 13
    # upper = False
    # lower = False
    # num = True

    length = int(request.GET.get('length'))
    upper = bool(request.GET.get('uperCase'))
    lower = bool(request.GET.get('lowerCase'))
    num = bool(request.GET.get('number'))
    spclChr = bool(request.GET.get('specialChar'))

    theName = str(request.GET.get('name'))

    theMotherList = []

    if upper:
        theMotherList.append(uperCase)
    if lower:
        theMotherList.append(lowerCase)
    if num:
        theMotherList.append(number)
    if spclChr:
        theMotherList.append(specialChar)

    for i in range(length):
        thePassword += random.choice(random.choice(theMotherList))

        # thePassword += random.choice(lowerCase)
    

    return render(request, 'sampleApp/passwordView.html', {'thePassword' : thePassword, 'theName': theName})


# Create your views here.
