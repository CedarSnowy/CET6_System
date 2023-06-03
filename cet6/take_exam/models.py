from django.db import models

from django.db import models
from django.urls import reverse

# Create your models here.


class SubjectiveQuestions(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=1000, blank=True, null=True)
    # answer = models.CharField(blank=True, null=True)
    score = models.FloatField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "subjective_questions"


class SubjectiveAnswers(models.Model):
    examinee_id = models.IntegerField()
    paper_id = models.IntegerField()
    question_id = models.IntegerField()
    answer = models.CharField(max_length=1000)


class ObjectiveQuestions(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=1000, blank=True, null=True)
    option_a = models.CharField(max_length=500)
    option_b = models.CharField(max_length=500)
    option_c = models.CharField(max_length=500)
    option_d = models.CharField(max_length=500)
    # answer = models.CharField(blank=True, null=True)

    score = models.FloatField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "objective_questions"


class ObjectiveAnswers(models.Model):
    examinee_id = models.IntegerField()
    paper_id = models.IntegerField()
    question_id = models.IntegerField()
    answer = models.CharField(max_length=1)


class PaperQuestions(models.Model):
    OBJECTIVE = "objective"
    SUBJECTIVE = "subjective"
    QUESTION_TYPES = (
        (OBJECTIVE, "Objective"),
        (SUBJECTIVE, "Subjective"),
    )

    id = models.IntegerField(primary_key=True)
    paper_id = models.IntegerField()
    question_id = models.IntegerField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

    class Meta:
        managed = True
        db_table = "paper_question"
