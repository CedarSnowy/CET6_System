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
from User_Manage.views import user_login, user_register, per_info, homepage
from Paper_Modification.models import (
    Paper,
    PaperQuestion,
    SubjectiveQuestion,
    SubjectiveAnswer,
    ObjectiveQuestion,
    ObjectiveAnswer,
)
from Exam_Manage.models import ExamInformation  # 后台管理员_考试信息管理类
from Exam_Manage.models import ExamScore
from take_exam.views import get_questions_by_paper, submit_answers


class ExamInformation_dataCenterAdmin(admin.ModelAdmin):
    list_display = ("exam_id", "exam_name", "exam_time", "location", "fee", "paper")


class ExamScore_dataCenterAdmin(admin.ModelAdmin):
    list_display = ("id_card_no", "exam", "score", "publish_date")


class Papers_dataCenterAdmin(admin.ModelAdmin):
    """
    试题
    """

    list_display = ("id", "paper_name", "total_score", "create_time")


class PaperQuestion_dataCenterAdmin(admin.ModelAdmin):
    """
    试卷考题展示
    """

    list_display = ("paper", "question", "question_type")


class SubjectiveQuestion_dataCenterAdmin(admin.ModelAdmin):
    """
    主观题
    """

    list_display = ("id", "question", "answer", "score", "create_time")


class SubjectiveAnswer_dataCenterAdmin(admin.ModelAdmin):
    """
    主观题答案
    """

    list_display = ("examinee", "paper", "question", "answer", "score")


class ObjectiveQuestion_dataCenterAdmin(admin.ModelAdmin):
    """
    客观题
    """

    list_display = (
        "id",
        "question",
        "option_a",
        "option_b",
        "option_c",
        "option_d",
        "answer_option",
        "score",
        "create_time",
    )


class ObjectiveAnswer_dataCenterAdmin(admin.ModelAdmin):
    """
    客观题答案
    """

    list_display = ("examinee", "paper", "question", "answer", "score")


admin.site.register(ExamInformation, ExamInformation_dataCenterAdmin)  # 注册
admin.site.register(ExamScore, ExamScore_dataCenterAdmin)
admin.site.register(Paper, Papers_dataCenterAdmin)  # 试卷
admin.site.register(PaperQuestion, PaperQuestion_dataCenterAdmin)
admin.site.register(SubjectiveQuestion, SubjectiveQuestion_dataCenterAdmin)
admin.site.register(SubjectiveAnswer, SubjectiveAnswer_dataCenterAdmin)
admin.site.register(ObjectiveQuestion, ObjectiveQuestion_dataCenterAdmin)
admin.site.register(ObjectiveAnswer, ObjectiveAnswer_dataCenterAdmin)


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
    path("user/login", user_login),
    path("user/register", user_register),
    path("homepage/<int:nid>/", homepage),
    path("homepage/<int:nid>/perinfo", per_info),
    path("homepage/<int:nid>/taking_exam", get_questions_by_paper, name="taking_exam"),
    path("submit_answers/", submit_answers, name="submit_answers"),
]
