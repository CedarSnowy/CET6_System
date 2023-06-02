from django.shortcuts import render
from .models import ExamInformation


# Create your views here.
def choose_exam(request):
    exams_list = ExamInformation.objects.all()
    return render(request, "exam_list.html", {"exams": exams_list})
