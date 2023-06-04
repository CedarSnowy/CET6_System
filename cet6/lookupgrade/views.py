from django.shortcuts import render, redirect

# Create your views here.
from lookupgrade import models


def lookupgrades(request,nid):
    flag=0
    if request.method=="GET":
        return render(request, "look_up_grades.html")
    else:
        #去请求体中获取数据，再进行校验
        #idno=request.POST.get('idno')
        idno=nid
        examid=request.POST.get('examid')
        queryset = models.ExamScore.objects.filter(**{"id_card_no":idno,"exam_id":int(examid)})
        #假设60分及格
        if queryset.exists():
            print("success")
            flag=1
        if flag==1:
            if queryset.first().score > 60:
                ispass = '通过!'
            else:
                ispass = '未通过!'
            score=queryset.first().score
            return render(request,"showgrades.html",{'score':score,'idcard':idno,'examid':examid,'ispass':ispass})
        else:
            return render(request,"look_up_grades.html",{"error":"身份证或考试号码错误,请重新确认"})