from django.db import models

# Create your models here.

DECISION = (
    (0, 'No'),
    (1, 'Yes')
)


class Detail(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=30, null=True)
    phone = models.CharField(max_length=10, null=True)
    city = models.CharField(max_length=30, null=True)
    landmark = models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=30,null=True)
    Age = models.PositiveIntegerField(null=True)
    fever =  models.PositiveIntegerField(choices=DECISION, null=True)
    cough =  models.PositiveIntegerField(choices=DECISION, null=True)
    runny_nose =  models.PositiveIntegerField(choices=DECISION, null=True)
    muscle_soreness =  models.PositiveIntegerField(choices=DECISION, null=True)
    pneumonia =  models.PositiveIntegerField(choices=DECISION, null=True)
    diarrhea =  models.PositiveIntegerField(choices=DECISION, null=True)
    lung_infection =  models.PositiveIntegerField(choices=DECISION, null=True)
    travel_history =  models.PositiveIntegerField(choices=DECISION, null=True)
    isolation_treatment = models.PositiveIntegerField(choices=DECISION, null=True)
    prediction = models.CharField(max_length=30,null=True)
    SeverityIndex = models.CharField(max_length=30,null=True)

class student(models.Model):
    name = models.CharField(max_length=30, null=True)
    rollno  = models.PositiveIntegerField(null=True)
    marks  = models.PositiveIntegerField(null=True)