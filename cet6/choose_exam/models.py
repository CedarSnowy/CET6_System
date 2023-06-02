from django.db import models
from django.urls import reverse

# Create your models here.


class ExamInformation(models.Model):
    exam_id = models.IntegerField(primary_key=True)
    exam_name = models.CharField(max_length=50, blank=True, null=True)
    exam_time = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    @staticmethod
    def __str__(self):
        return self.exam_name

    class Meta:
        managed = True
        db_table = "exam_information"
