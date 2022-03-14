"""OSDC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pd/', views.pd, name="pd"),
    path('mh/', views.mh, name="mh"),
    path('t/', views.t, name="t"),
    path('ce/', views.ce, name="ce"),
    path('v/', views.v, name="v"),
    path('ct/', views.ct, name="ct"),
    path('dc/', views.dc, name="dc"),
    path('gh/', views.gh, name="gh"),
    path('sh/', views.sh, name="sh"),
    path('prg/', views.prg, name="prg"),
    
    path('pdview/', views.pdview, name="pdview"),
    path('mhview/', views.mhview, name="mhview"),
    path('tview/', views.tview, name="tview"),
    path('ceview/', views.ceview, name="ceview"),
    path('vview/', views.vview, name="vview"),
    path('ctview/', views.ctview, name="ctview"),
    path('dcview/', views.dcview, name="dcview"),
    path('ghview/', views.ghview, name="ghview"),
    path('shview/', views.shview, name="shview"),

    path('home/', views.home, name="home"),
    path('register/', v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('', views.index, name="index"),

    path('chart/', views.chart, name='chart'),
    path('data1/', views.data, name='data'),

    path('vdata/', views.vdata, name='vdata'),
    path('tbdata/', views.tbdata, name='tbdata'),
    path('cedata/', views.cedata, name='cedata'),
    path('mhdata/', views.mhdata, name='mhdata'),
    path('pddata/', views.pddata, name='pddata'),
    path('ghdata/', views.ghdata, name='ghdata'),
    path('shdata/', views.shdata, name='shdata'),
    path('dcdata/', views.dcdata, name='dcdata'),
]
