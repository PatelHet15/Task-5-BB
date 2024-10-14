# models.py
from django.contrib.postgres.fields import ArrayField
from django.db import models

class QuizQuestion(models.Model):
    question_no = models.PositiveIntegerField(unique=True)
    question = models.CharField(max_length=255)  
    options = ArrayField( 
        models.CharField(max_length=255),  
        size=5  
    )
    right_answer = models.CharField(max_length=255) 

    def __str__(self):
        return self.question
