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
from django.contrib.auth import logout

_nid = 310110199001011234
_paper_id = 1


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
    questions.append(objective_questions)
    questions.append(subjective_questions)
    return render(request, "taking_exam.html", {"questions_list": questions})


def submit_answers(request):
    print("_nid", _nid, "_paper", _paper_id)
    if request.method == "POST":
        # 获取所有的客观题 id 和答案
        objective_choices = {}
        for key in request.POST:
            if not key.endswith("-choice"):
                continue
            objective_choices[key[:-7]] = request.POST[key]
        print(objective_choices)

        # 获取所有的主观题 id 和答案
        subjective_answers = {}
        for key in request.POST:
            if not key.endswith("-text"):
                continue
            answer_id = key[:-5]
            answer_content = request.POST[key]
            subjective_answers[answer_id] = answer_content
        print(subjective_answers)

        # 提交客观题答案
        for question_id, choice in objective_choices.items():
            # 检查是否已存在
            existing_answer = ObjectiveAnswers.objects.filter(
                examinee_id=_nid,
                paper_id=_paper_id,
                question_id=question_id,
            ).first()

            if existing_answer:
                print(f"Answer already exists: id={existing_answer.id}")
            else:
                answer = ObjectiveAnswers.objects.create(
                    examinee_id=_nid,
                    paper_id=_paper_id,
                    question_id=question_id,
                    answer=choice,
                    score=0,
                )
                print(f"Saved answer: id={answer.id}")

        # 提交主观题答案
        for answer_id, content in subjective_answers.items():
            # 检查是否已存在
            existing_answer = SubjectiveAnswers.objects.filter(
                examinee_id=_nid,
                paper_id=_paper_id,
                question_id=question_id,
            ).first()

            if existing_answer:
                print(f"Answer already exists: id={existing_answer.id}")
            else:
                answer = SubjectiveAnswers.objects.create(
                    examinee_id=_nid,
                    paper_id=_paper_id,
                    question_id=question_id,
                    answer=content,
                    score=0,
                )
                print(f"Saved answer: id={answer.id}")

        messages.success(request, "提交成功！")
        return redirect("logout")
    else:
        return render(request, "taking_exam")


def logout_view(request):
    logout(request)
    return render(request, "logout.html")
