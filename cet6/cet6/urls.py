"""cet6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

# 解决方案来自于：https://blog.csdn.net/shizheng_Li/article/details/124568350
from django.urls import re_path as url
from lookupgrade.views import lookupgrades
from payment.views import information_of_registration, QRcode, pay_done
from choose_exam.views import choose_exam
from Search_APPLY.views import search_exam_info, submit_enroll_info

urlpatterns = [
    path("admin/", admin.site.urls),
    # url(r'^showStudents$', showStudents),
    # url(r'^payment$', information_of_registration),
    path("payment/", information_of_registration),
    path("payment2/", QRcode),
    path("payment_done/", pay_done),
    path("lookupgrades/", lookupgrades),
    path("choose_exam/", choose_exam),
    path("search_exam_info/", search_exam_info),
    path("submit_enroll_info/", submit_enroll_info),
]
