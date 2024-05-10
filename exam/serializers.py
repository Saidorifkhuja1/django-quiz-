from rest_framework import serializers
from .models import Exam, Quizzes, Question, Answer
from account.serializers import TeacherSerializer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'answer_text', 'is_right']

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'quiz', 'technique', 'title', 'answer']

class QuizzesSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quizzes
        fields = ['id', 'title', 'category', 'data_created', 'questions']

class ExamSerializer(serializers.ModelSerializer):
    quizzes = QuizzesSerializer(many=True, read_only=True)
    teacher = TeacherSerializer()

    class Meta:
        model = Exam
        fields = ['id', 'name', 'description', 'teacher', 'start_date', 'end_date', 'time_limit_minutes', 'quizzes']
