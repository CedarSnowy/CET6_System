from django.shortcuts import render, HttpResponse, redirect
from User_Manage import models
from django import forms

# Create your views here.


# 用户登录界面
def user_login(request):
    # return HttpResponse("欢迎！请登录")
    if request.method == "GET":
        return render(request, "user_login.html")

    phone_number = request.POST.get("login_number", None)
    password = request.POST.get("login_pwd", None)

    data_list = models.Examinee.objects.all()
    for obj in data_list:
        if obj.phone_number == phone_number and obj.password == password:
            obj = models.Examinee.objects.filter(password=password).first()
            # return redirect("/homepage/{}/perinfo".format(obj.id_card_no))
            return redirect("/homepage/{}/".format(obj.id_card_no))
            # return redirect("/homepage/")

    return HttpResponse("登录失败")


# 用户注册界面
def user_register(request):
    # return HttpResponse("欢迎！请登录")
    if request.method == "GET":
        return render(request, "user_register.html")

    # 获取输入表单信息
    register_name = request.POST.get("register_name", None)
    register_gender = request.POST.get("register_gender", None)
    register_id = request.POST.get("register_id", None)
    register_phone = request.POST.get("register_phone", None)
    register_pwd = request.POST.get("register_pwd2", None)

    # 添加到数据库
    # print(obj.id_card_no, obj.gender, obj.password, obj.name, obj.phone_number)
    models.Examinee.objects.create(
        id_card_no=register_id,
        gender=register_gender,
        password=register_pwd,
        name=register_name,
        phone_number=register_phone,
    )

    data_list = models.Examinee.objects.all()
    for obj in data_list:
        print(obj.id_card_no, obj.gender, obj.password, obj.name, obj.phone_number)

    # 跳转到登录界面
    return redirect("/user/login")


# 首页
def homepage(request, nid):
    if request.method == "GET":
        return render(request, "homepage.html")
    # return HttpResponse('Hello World!')

# 个人信息页面
def per_info(request, nid):
    obj = models.Examinee.objects.filter(id_card_no=nid).first()

    if request.method == "GET":
        # return render(request, "per_info.html", {"row_obj": row_obj})
        return render(request, "per_info.html", {"obj": obj})
    # form1 = UserModelForm(instance=row_obj)

    name = request.POST.get("username", None)
    gender = request.POST.get("gender", None)
    id_number = request.POST.get("id_number", None)
    phone = request.POST.get("telephone", None)
    pwd = request.POST.get("password", None)

    models.Examinee.objects.filter(id_card_no=nid).update(
        name=name, gender=gender, phone_number=phone, password=pwd
    )
    obj = models.Examinee.objects.filter(id_card_no=id_number).first()
    return render(request, "per_info.html", {"obj": obj})
