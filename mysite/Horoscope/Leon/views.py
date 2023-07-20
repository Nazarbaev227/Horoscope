from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'first/home.html')


def Aries(request):
    return render(request, 'first/Aries.html')


def Taurus(request):
    return HttpResponse("Телец")


def Gemini(request):
    return HttpResponse("Близнецы")


def Cancer(request):
    return HttpResponse("Рак")


def Leo(request):
    return HttpResponse("Лев")


def Virgo(request):
    return HttpResponse("Дева")


def Libra(request):
    return HttpResponse("Весы")


def Scorpio(request):
    return HttpResponse("Скорпион")


def Ophiuchus(request):
    return HttpResponse("Змееносец")


def Sagittarius(request):
    return HttpResponse("Стрелец")


def Capricorn(request):
    return HttpResponse("Козерог")


def Aquarius(request):
    return HttpResponse("Водолей")


def Pisces(request):
    return HttpResponse("Рыбы")


def Kapibara(request):
    return HttpResponse("<a href='https://www.youtube.com/watch?v=zz7IIN_MAN4&ab_channel=UncleKnuckles'>Капибара</a>")
