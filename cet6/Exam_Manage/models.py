# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    id_card_no = models.CharField(primary_key=True, max_length=18)
    password = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Enrollment(models.Model):
    id_card_no = models.OneToOneField('Examinee', models.DO_NOTHING, db_column='id_card_no', primary_key=True)  # The composite primary key (id_card_no, exam_id) found, that is not supported. The first column is selected.
    exam = models.ForeignKey('ExamInformation', models.DO_NOTHING)
    enrollment_time = models.DateTimeField(blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enrollment'
        unique_together = (('id_card_no', 'exam'),)


class ExamInformation(models.Model):
    exam_id = models.IntegerField(primary_key=True)  # The composite primary key (exam_id, paper_id) found, that is not supported. The first column is selected.
    def __str__(self):
        return str(self.exam_id)
    exam_name = models.CharField(max_length=50, blank=True, null=True)
    exam_time = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    paper = models.ForeignKey('Papers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'exam_information'
        unique_together = (('exam_id', 'paper'),)


class ExamScore(models.Model):
    id_card_no = models.OneToOneField('Examinee', models.DO_NOTHING, db_column='id_card_no', primary_key=True)  # The composite primary key (id_card_no, exam_id) found, that is not supported. The first column is selected.
    def __str__(self):
        return str(self.id_card_no)
    exam = models.ForeignKey(ExamInformation, models.DO_NOTHING)
    def __str__(self):
        return str(self.exam)
    score = models.FloatField(blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_score'
        unique_together = (('id_card_no', 'exam'),)


class Examinee(models.Model):
    id_card_no = models.CharField(primary_key=True, max_length=18)
    def __str__(self):
        return str(self.id_card_no)
    gender = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'examinee'


class ObjectiveAnswers(models.Model):
    examinee = models.OneToOneField(Examinee, models.DO_NOTHING, primary_key=True)  # The composite primary key (examinee_id, paper_id, question_id) found, that is not supported. The first column is selected.
    paper = models.ForeignKey('Papers', models.DO_NOTHING)
    question = models.ForeignKey('ObjectiveQuestions', models.DO_NOTHING)
    answer = models.CharField(max_length=1, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objective_answers'
        unique_together = (('examinee', 'paper', 'question'),)


class ObjectiveQuestions(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=1000, blank=True, null=True)
    option_a = models.CharField(max_length=500, blank=True, null=True)
    option_b = models.CharField(max_length=500, blank=True, null=True)
    option_c = models.CharField(max_length=500, blank=True, null=True)
    option_d = models.CharField(max_length=500, blank=True, null=True)
    answer_option = models.CharField(max_length=1, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objective_questions'


class PaperQuestion(models.Model):
    paper = models.ForeignKey('Papers', models.DO_NOTHING)
    question = models.ForeignKey('SubjectiveQuestions', models.DO_NOTHING)
    question_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'paper_question'


class Papers(models.Model):
    id = models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.id)
    paper_name = models.CharField(max_length=100, blank=True, null=True)
    total_score = models.FloatField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'papers'


class Payment(models.Model):
    id_card_no = models.OneToOneField(Examinee, models.DO_NOTHING, db_column='id_card_no', primary_key=True)  # The composite primary key (id_card_no, exam_id) found, that is not supported. The first column is selected.
    exam = models.ForeignKey(ExamInformation, models.DO_NOTHING)
    payment_time = models.DateTimeField(blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'
        unique_together = (('id_card_no', 'exam'),)


class SubjectiveAnswers(models.Model):
    examinee = models.OneToOneField(Examinee, models.DO_NOTHING, primary_key=True)  # The composite primary key (examinee_id, paper_id, question_id) found, that is not supported. The first column is selected.
    paper = models.ForeignKey(Papers, models.DO_NOTHING)
    question = models.ForeignKey('SubjectiveQuestions', models.DO_NOTHING)
    answer = models.CharField(max_length=1000, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subjective_answers'
        unique_together = (('examinee', 'paper', 'question'),)


class SubjectiveQuestions(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=1000, blank=True, null=True)
    answer = models.CharField(max_length=1000, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subjective_questions'
