
from django.contrib import admin
from django.urls import path
from sampleApp import views

urlpatterns = [
    path('afnan/', admin.site.urls),
    path('', views.home, name='home'),
    path('passview/', views.passView, name='thePassword'),
]
