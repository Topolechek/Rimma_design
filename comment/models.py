from django.utils import timezone
from django.db import models
now = timezone.now()

class Comment(models.Model):
    commentator_name = models.CharField('Имя', max_length=100, default="Аноним")
    comment_text = models.CharField('Отзыв', max_length=1000)
    date = models.DateTimeField('Дата', default=timezone.now)

    def __str__(self):                     # Отображает title в админке
        return self.commentator_name