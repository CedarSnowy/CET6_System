from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

from django.db import models

class Admin(models.Model):
    id_card_no = models.CharField(primary_key=True, max_length=18)
    password = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class Enrollment(models.Model):
    id_card_no = models.OneToOneField('Examinee', models.DO_NOTHING, db_column='id_card_no', primary_key=True)  # The
    # composite primary key (id_card_no, exam_id) found, that is not supported. The first column is selected.
    exam = models.ForeignKey('ExamInformation', models.DO_NOTHING)
    enrollment_time = models.DateTimeField(blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enrollment'
        unique_together = (('id_card_no', 'exam'),)


class ExamInformation(models.Model):
    exam_id = models.IntegerField(primary_key=True)
    exam_name = models.CharField(max_length=50, blank=True, null=True)
    exam_time = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_information'


class ExamScore(models.Model):
    id_card_no = models.OneToOneField('Examinee', models.DO_NOTHING, db_column='id_card_no', primary_key=True)  # The composite primary key (id_card_no, exam_id) found, that is not supported. The first column is selected.
    exam = models.ForeignKey(ExamInformation, models.DO_NOTHING)
    score = models.FloatField(blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_score'
        unique_together = (('id_card_no', 'exam'),)


class Examinee(models.Model):
    id_card_no = models.CharField(primary_key=True, max_length=18)
    gender = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'examinee'


class Payment(models.Model):
    id_card_no = models.OneToOneField(Examinee, models.DO_NOTHING, db_column='id_card_no', primary_key=True)  # The composite primary key (id_card_no, exam_id) found, that is not supported. The first column is selected.
    exam = models.ForeignKey(ExamInformation, models.DO_NOTHING)
    payment_time = models.DateTimeField(blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'
        unique_together = (('id_card_no', 'exam'),)

