# from django.db import models


# class Admin(models.Model):
#     id_card_no = models.CharField(primary_key=True, max_length=18)
#     password = models.CharField(max_length=255, blank=True, null=True)
#     name = models.CharField(max_length=20, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = "admin"


# class Enrollment(models.Model):
#     id_card_no = models.OneToOneField(
#         "Examinee", models.DO_NOTHING, db_column="id_card_no", primary_key=True
#     )  # The composite primary key (id_card_no, exam_id) found, that is not supported. The first column is selected.
#     exam = models.ForeignKey("ExamInformation", models.DO_NOTHING)
#     enrollment_time = models.DateTimeField(blank=True, null=True)
#     payment_status = models.CharField(max_length=20, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = "enrollment"
#         unique_together = (("id_card_no", "exam"),)


# class ExamInformation(models.Model):
#     exam_id = models.IntegerField(primary_key=True)
#     exam_name = models.CharField(max_length=50, blank=True, null=True)
#     exam_time = models.DateTimeField(blank=True, null=True)
#     location = models.CharField(max_length=100, blank=True, null=True)
#     fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = "exam_information"


# class ExamScore(models.Model):
#     id_card_no = models.OneToOneField(
#         "Examinee", models.DO_NOTHING, db_column="id_card_no", primary_key=True
#     )  # The composite primary key (id_card_no, exam_id) found, that is not supported. The first column is selected.
#     exam = models.ForeignKey(ExamInformation, models.DO_NOTHING)
#     score = models.FloatField(blank=True, null=True)
#     publish_date = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = "exam_score"
#         unique_together = (("id_card_no", "exam"),)


# class Examinee(models.Model):
#     id_card_no = models.CharField(primary_key=True, max_length=18)
#     gender = models.CharField(max_length=10, blank=True, null=True)
#     password = models.CharField(max_length=255, blank=True, null=True)
#     name = models.CharField(max_length=20, blank=True, null=True)
#     phone_number = models.CharField(max_length=11, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = "examinee"


# class Payment(models.Model):
#     id_card_no = models.OneToOneField(
#         Examinee, models.DO_NOTHING, db_column="id_card_no", primary_key=True
#     )  # The composite primary key (id_card_no, exam_id) found, that is not supported. The first column is selected.
#     exam = models.ForeignKey(ExamInformation, models.DO_NOTHING)
#     payment_time = models.DateTimeField(blank=True, null=True)
#     payment_amount = models.DecimalField(
#         max_digits=10, decimal_places=2, blank=True, null=True
#     )

#     class Meta:
#         managed = False
#         db_table = "payment"
#         unique_together = (("id_card_no", "exam"),)


# class SubjectiveAnswers(models.Model):
#     id = models.IntegerField(primary_key=True)
#     examinee_id = models.CharField(max_length=18)
#     paper_id = models.IntegerField()
#     question_id = models.IntegerField()
#     answer = models.CharField(max_length=1000)
#     score = models.FloatField()

#     class Meta:
#         managed = True
#         db_table = "subjective_answers"
#         # unique_together = (("examinee_id", "paper_id", "question_id"),)

#     def __str__(self) -> str:
#         return f"{self.id} - {self.examinee_id} - {self.paper_id} - {self.question_id} - {self.answer} - {self.score}"


# class ObjectiveQuestions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     question = models.CharField(max_length=1000, blank=True, null=True)
#     option_a = models.CharField(max_length=500)
#     option_b = models.CharField(max_length=500)
#     option_c = models.CharField(max_length=500)
#     option_d = models.CharField(max_length=500)
#     answer_option = models.CharField(max_length=1, blank=True, null=True)
#     score = models.FloatField()

#     class Meta:
#         managed = True
#         db_table = "objective_questions"

#     def __str__(self):
#         return f"{self.id} - {self.question} - {self.answer_option} - {self.score}"


# class ObjectiveAnswers(models.Model):
#     id = models.IntegerField(primary_key=True)
#     examinee_id = models.CharField(max_length=18)
#     paper_id = models.IntegerField()
#     question_id = models.IntegerField()
#     answer = models.CharField(max_length=1)
#     score = models.FloatField()

#     class Meta:
#         managed = True
#         db_table = "objective_answers"
#         # unique_together = (("examinee_id", "paper_id", "question_id"),)

#     def __str__(self) -> str:
#         return f"{self.id} - {self.examinee_id} - {self.paper_id} - {self.question_id} - {self.answer} - {self.score}"
