from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import Teacher


class Exam(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    time_limit_minutes = models.PositiveIntegerField(null=True, blank=True,help_text='Vaqt limiti minutlarda bo\'lishi kerak ')
    def __str__(self):
        return self.name

class Quizzes(models.Model):
    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')
        ordering = ['id']
    title = models.CharField(max_length=255, default=_('New Quiz'), verbose_name=_('Quiz Title'))
    category = models.ForeignKey(Exam, default=1, on_delete=models.DO_NOTHING)
    data_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title





class Question(models.Model):
    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['id']

    TYPE = ((0, _('Multiple Choice')),)
    quiz = models.ForeignKey(Quizzes, related_name='questions',  on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_('Type of Question'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))


    def __str__(self):
        return self.title
class Answer(models.Model):
    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')
        ordering = ['id']

    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name=_('Answer Text'))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
