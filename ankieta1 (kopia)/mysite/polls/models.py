import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)#creates a character field up to 200 signs
    pub_date = models.DateTimeField('date published')#creates a date time field

    def __unicode__(self):              # __unicode__ on Python 2
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'	


class Choice(models.Model):
    question = models.ForeignKey(Question)#thanks to that each choice is realted to questions.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.choice_text

