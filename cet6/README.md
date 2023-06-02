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
## 7.提交
