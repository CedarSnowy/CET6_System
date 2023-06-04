from datetime import datetime

from django.db.models import DateTimeField
from django.shortcuts import render, redirect
from payment import models

# Create your views here.
#解决图片不出现问题：https://blog.csdn.net/pxyyoona/article/details/109052141
def information_of_registration(request,nid):
    #新增
    #models.Department.objects.create(**{"title":"123","count":18})

    #查询
    """
    queryset=models.Department.objects.all()
    queryset=models.Department.objects.filter(id__gt=0)#id>0
    queryset=models.Department.objects.filter(id=0).first()#id>0
    for obj in queryset:
        print(obj.id,obj.title,obj.count)
    """

    #删除
    """
    models.Department.objects.filter(id=0).delete()
    """

    #更新
    """
    models.Department.objects.filter(id=0).upgrade(count=99)  
    """



    #1.数据库获取

    #判断是post还是get请求
    if request.method=="GET":
        return render(request, "pay.html")
    else:
        #去请求体中获取数据，再进行校验
        #idno=request.POST.get('idno')
        idno=nid
        examid=request.POST.get('examid')
        #去数据库校验，用户名&密码的合法性
        #成果则跳转到后台管理页面/index  /index/
        #return redirect('/index/')
        #不成功再次看到上一个页面，提示用户名密码错误
        flag=0
        queryset = models.Enrollment.objects.filter(id_card_no=idno)
        queryset_for_fee = models.ExamInformation.objects.filter(exam_id=int(examid)).first()
        queryset_for_id= models.Examinee.objects.filter(id_card_no=idno).first()
        queryset_for_exam = models.ExamInformation.objects.filter(exam_id=int(examid)).first()
        if_exist=models.Payment.objects.filter(**{"id_card_no": idno, "exam_id": int(examid)})
        for obj in queryset:
            if obj.exam_id==int(examid) :
                print("success")
                if if_exist.exists():
                    return render(request, "pay.html", {"error": "重复缴费"})
                else :
                    models.Payment.objects.create(id_card_no=queryset_for_id,exam=queryset_for_exam,payment_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'), payment_amount=queryset_for_fee.fee)
                #报名信息改成已支付状态
                models.Enrollment.objects.filter(**{"id_card_no": idno, "exam_id": int(examid)}).update(payment_status="已支付")
                flag=1
        if flag==1:
            #return render(request,"qrcode.html")
            return redirect("/homepage/{}/payment2".format(nid))
        else:
            return render(request,"pay.html",{"error":"身份证或考试号码错误,请重新确认是否注册或报名"})
    #2.打开文件读取内容
    #3.模板渲染-》文本替换
    #return render(request, "pay.html", {"messgage": "这里是标题", "data_list":data, "xx":mapping})

def QRcode(request,nid):
    return render(request, "qrcode.html")
def pay_done(request,nid):

    return render(request, "pay_done.html")