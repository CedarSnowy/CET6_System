from django.test import TestCase
from .models import (
    SubjectiveQuestions,
    ObjectiveQuestions,
    SubjectiveAnswers,
    ObjectiveAnswers,
    PaperQuestions,
)


class ModelTestCase(TestCase):
    def setUp(self):
        """
        创建测试样例数据
        """
        self.subjective_question = SubjectiveQuestions.objects.create(
            id=3, question="What is your favorite color?", answer="Blue", score=10.0
        )
        self.objective_question = ObjectiveQuestions.objects.create(
            id=1,
            question="What is the capital of France?",
            option_a="London",
            option_b="Paris",
            option_c="Berlin",
            option_d="Madrid",
            answer_option="b",
            score=5.0,
        )
        self.subjective_answer = SubjectiveAnswers.objects.create(
            id=1,
            examinee_id="ABC123",
            paper_id=1,
            question_id=1,
            answer="This is my answer",
            score=4.5,
        )

        self.objective_answer = ObjectiveAnswers.objects.create(
            id=1, examinee_id="ABC123", paper_id=1, question_id=1, answer="a", score=2.0
        )
        self.paper_question = PaperQuestions.objects.create(
            id=1, paper_id=1, question_id=1, question_type="objective"
        )

    """
    定义每个类的测试函数，检查__str__()返回是否正确
    """

    def test_subjective_question_creation(self):
        self.assertTrue(isinstance(self.subjective_question, SubjectiveQuestions))
        self.assertEqual(
            self.subjective_question.__str__(),
            "3 - What is your favorite color? - Blue - 10.0",
        )

    def test_objective_question_creation(self):
        self.assertTrue(isinstance(self.objective_question, ObjectiveQuestions))
        self.assertEqual(
            self.objective_question.__str__(),
            "1 - What is the capital of France? - b - 5.0",
        )

    def test_objective_answer_creation(self):
        self.assertTrue(isinstance(self.objective_answer, ObjectiveAnswers))
        self.assertEqual(
            self.objective_answer.__str__(),
            "1 - ABC123 - 1 - 1 - a - 2.0",
        )

    def test_subjective_answer_creation(self):
        self.assertTrue(isinstance(self.subjective_answer, SubjectiveAnswers))
        self.assertEqual(
            self.subjective_answer.__str__(),
            "1 - ABC123 - 1 - 1 - This is my answer - 4.5",
        )

    def test_paper_question_creation(self):
        self.assertTrue(isinstance(self.paper_question, PaperQuestions))
        self.assertEqual(
            self.paper_question.__str__(),
            "1 - 1 - 1 - objective",
        )
