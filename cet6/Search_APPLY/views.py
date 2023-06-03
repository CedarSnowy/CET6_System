from datetime import datetime

from Search_APPLY import models
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse


def say_hello(request):
    s = 'Hello World!'
    current_time = datetime.datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)


def showStudents(request):
    list = [{id: 1, 'name': 'Jack'}, {id: 2, 'name': 'Rose'}]
    return render(request, 'search_exam.html', {'students': list})


def search_exam_info(request):
    """
    1. 打印所有可报名的考试信息
    2. 并在最下面添加报名按钮
    ** 难点： 把考试信息数据库的内容都读进来，然后作为参数传给前端，并且进行打印
    """
    data = models.ExamInformation.objects.all()  # 读取数据库中所有的元素
    return render(request, "search_exam.html", {'data': data})


def submit_enroll_info(request):
    """
    1. 考试id, 身份证
    2. 默认支付状态为未支付(在这里要不要跳到支付页面？)
    3. 系统计算加入时间
    """
    # 判断是post还是get请求
    if request.method == "GET":
        return render(request, "submit_enroll_info.html")  # 进入考试报名
    else:
        # 去请求体中获取数据，再进行校验
        idno = request.POST.get('idno')  # 考生id
        examid = request.POST.get('examid')  # 考试id
        # 去数据库校验，用户名&密码的合法性
        # 成功则跳转到后台管理页面/index  /index/
        # return redirect('/index/')
        # 不成功再次看到上一个页面，提示用户名密码错误

        if_exist = models.Enrollment.objects.filter(**{"id_card_no": idno, "exam_id": int(examid)})  # 是否已经报名
        if if_exist.exists():  # 如果已经报名了，直接提示
            return render(request, "submit_enroll_info.html", {"error": "重复报名"})
        else:  # 如果还没有报名，验证id_card_no和exam_id的合法性
            queryset_for_id = models.Examinee.objects.filter(id_card_no=idno).first()
            queryset_for_exam = models.ExamInformation.objects.filter(exam_id=int(examid)).first()
            if queryset_for_id is None or queryset_for_exam is None:  # 如果user_id或exam_id不存在
                return render(request, "submit_enroll_info.html", {"error": "身份证或考试号码错误,请重新确认"})
            else:  # 如果均存在且没报过名
                models.Enrollment.objects.create(id_card_no=queryset_for_id, exam=queryset_for_exam,
                                                 enrollment_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                 payment_status="未支付")
                return render(request, "submit_enroll_info.html", {"error": "报名成功，请及时缴费！"})
