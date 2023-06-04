## 1.拉取仓库
## 2.在命令行中创建新的应用
```
django-admin startapp <your_app_name>
```
## 3.在cet6/settings.py的INSTALLED_APPS中，添加新创建的app_name
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Exam_Manage",  # 考试管理页面
    "Score_Modification",  # 成绩信息修改页面
    "payment",  # 支付页面
    "lookupgrade",  # 查分页面
]
```
## 4.在cet6/setting.py的DATABASES中，修改为本地的数据库信息
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",  # 数据库的类型
        "NAME": "cet6",  # 所使用的的数据库的名字
        "USER": "root",  # 数据库服务器的用户
        "PASSWORD": "",
        "HOST": "localhost",  # 主机
        "PORT": "3306",  # 端口
    }
}
```
## 5.在cet6/setting.py的TEMPLATES中，加入该行代码
```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # 加入这一行
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```
## 6.在自己的app文件夹中编写代码

## 7.代码修改
### (1) 在url.s中修改路径格式，参照如下:
```python
path("homepage/<int:nid>", homepage),
path("homepage/<int:nid>/perinfo", per_info),
path("homepage/<int:nid>/xx", xx),
```
### 与在User_Manage/view.py的homepage函数中添加参数nid一样，在自己对应的view.py中添加参数
```python
def homepage(request, nid):
    if request.method == "GET":
        return render(request, "homepage.html")
```

### (2) view.py的相关修改可参照User_Manage/views.py文件
```python
# eg.页面跳转  user_login()函数中用到
redirect("/homepage/{}/".format(obj.id_card_no))
```
### (3) 在homepage.html中的其他按钮位置添加类似url参数
```html
<div class="bb">
     <!--        /homepage/<int:nid>/perinfo"  仅需添加最后的一部分-->
    <button onclick='location.href=("perinfo")' type="button" class="mybb">个人信息</button>
    
</div>
```

## 8.提交
