from django.db import models

from django.db import models
from django.urls import reverse

# Create your models here.


class SubjectiveQuestions(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=1000, blank=True, null=True)
    answer = models.CharField(max_length=1000, blank=True, null=True)
    score = models.FloatField()

    class Meta:
        managed = True
        db_table = "subjective_questions"


class SubjectiveAnswers(models.Model):
    id = models.IntegerField(primary_key=True)
    examinee_id = models.CharField(max_length=18)
    paper_id = models.IntegerField()
    question_id = models.IntegerField()
    answer = models.CharField(max_length=1000)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = "subjective_answers"
        unique_together = (("examinee_id", "paper_id", "question_id"),)


class ObjectiveQuestions(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=1000, blank=True, null=True)
    option_a = models.CharField(max_length=500)
    option_b = models.CharField(max_length=500)
    option_c = models.CharField(max_length=500)
    option_d = models.CharField(max_length=500)
    answer_option = models.CharField(max_length=1, blank=True, null=True)
    score = models.FloatField()

    class Meta:
        managed = True
        db_table = "objective_questions"


class ObjectiveAnswers(models.Model):
    id = models.IntegerField(primary_key=True)
    examinee_id = models.CharField(max_length=18)
    paper_id = models.IntegerField()
    question_id = models.IntegerField()
    answer = models.CharField(max_length=1)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = "objective_answers"
        unique_together = (("examinee_id", "paper_id", "question_id"),)


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
