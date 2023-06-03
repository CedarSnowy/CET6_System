from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (
    ObjectiveQuestions,
    ObjectiveAnswers,
    SubjectiveQuestions,
    SubjectiveAnswers,
    PaperQuestions,
)

_nid = 0
_paper_id = 0


def homepage(request, nid):
    if request.method == "GET":
        return render(request, "homepage.html")


def get_questions_by_paper(request, nid, paper_id=1):
    global _nid, _paper_id
    _nid, _paper_id = nid, paper_id
    # 获取与指定试卷相关的问题
    paper_questions = PaperQuestions.objects.filter(paper_id=_paper_id)

    # 获取主观题和客观题的 ID 列表
    subjective_question_ids = [
        pq.id for pq in paper_questions if pq.id and pq.question_type == "subjective"
    ]
    objective_question_ids = [
        pq.id for pq in paper_questions if pq.id and pq.question_type == "objective"
    ]

    # 根据 ID 列表查询对象
    subjective_questions = SubjectiveQuestions.objects.filter(
        id__in=subjective_question_ids
    )
    objective_questions = ObjectiveQuestions.objects.filter(
        id__in=objective_question_ids
    )

    # 将查询结果保存到列表中并返回
    questions = []
    questions.append(subjective_questions)
    questions.append(objective_questions)
    return render(request, "taking_exam.html", {"questions_list": questions})


def submit_answers(request):
    if request.method == "POST":
        # 获取所有的客观题 id 和答案
        objective_choices = {}
        for key in request.POST:
            if not key.endswith("-choice"):
                continue
            objective_choices[key[:-7]] = request.POST[key]

        # 获取所有的主观题 id 和答案
        subjective_answers = {}
        for key in request.POST:
            if not key.endswith("-text"):
                continue
            answer_id = key[:-5]
            answer_content = request.POST[key]
            subjective_answers[answer_id] = answer_content

        # 提交客观题答案
        for question_id, choice in objective_choices.items():
            question = ObjectiveQuestions.objects.get(pk=question_id)
            ObjectiveAnswers.objects.create(
                examinee_id=_nid,
                paper_id=_paper_id,
                question_id=question_id,
                answer=choice,
                score=0,
            )

        # 提交主观题答案
        for answer_id, content in subjective_answers.items():
            answer = SubjectiveAnswers.objects.get(pk=answer_id)
            answer.subjective_answer = content
            answer.save()

        messages.success(request, "提交成功！")
        # return redirect("exam_result")

    return render(request, "homepage.html")
