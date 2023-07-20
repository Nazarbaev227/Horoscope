

from Leon import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('1', views.Aries),
    path('2', views.Taurus),
    path('3', views.Gemini),
    path('4', views.Cancer),
    path('5', views.Leo),
    path('6', views.Virgo),
    path('7', views.Libra),
    path('8', views.Scorpio),
    path('9', views.Ophiuchus),
    path('10', views.Sagittarius),
    path('11', views.Capricorn),
    path('12', views.Aquarius),
    path('13', views.Pisces),
    path('14', views.Kapibara),

]
