from django.shortcuts import render, redirect
from datetime import datetime
import os
import sys


# Create your views here.
from db_tables.models import (
    ExamInformation,
    ExamScore,
    SubjectiveAnswers,
    ObjectiveAnswers,
    ExamScore,
)


def stats_score(nid, examid):
    exam_info = ExamInformation.objects.filter(exam_id=examid).first()
    paper_id = int(exam_info.paper.id)

    try:
        # 筛选所有主观题分数
        subjective_scores = SubjectiveAnswers.objects.filter(
            examinee_id=nid, paper_id=paper_id
        ).values_list("score", flat=True)

        # 筛选所有客观题分数
        objective_scores = ObjectiveAnswers.objects.filter(
            examinee_id=nid, paper_id=paper_id
        ).values_list("score", flat=True)

        exam_score, created = ExamScore.objects.update_or_create(
            id_card_no=nid,
            exam=examid,
            defaults={
                "score": sum(subjective_scores) + sum(objective_scores),
                "pulish_data": datetime.now().date(),
            },
        )

    except AttributeError:
        return -1


def lookupgrades(request, nid):
    flag = 0
    if request.method == "GET":
        return render(request, "look_up_grades.html")
    else:
        # 去请求体中获取数据，再进行校验
        # idno=request.POST.get('idno')

        idno = nid
        examid = request.POST.get("examid")
        stats_score(idno, examid)
        queryset = ExamScore.objects.filter(
            **{"id_card_no": idno, "exam_id": int(examid)}
        )
        # 假设60分及格
        if queryset.exists():
            print("success")
            flag = 1
        if flag == 1:
            if queryset.first().score > 60:
                ispass = "通过!"
            else:
                ispass = "未通过!"
            score = queryset.first().score
            return render(
                request,
                "showgrades.html",
                {"score": score, "idcard": idno, "examid": examid, "ispass": ispass},
            )
        else:
            return render(request, "look_up_grades.html", {"error": "身份证或考试号码错误,请重新确认"})
