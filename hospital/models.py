from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

HOSPITAL_NAMES = (
    ('A','Bombay Hospital Mumbai'),
    ('B', 'Apollo Hospital, Bandra west Mumbai'),
)

YES_NO = (
    ('Y', 'Yes'),
    ('N', 'No')
)

CASE_TYPE = (
    ('E', 'Emergency'),
    ('N', 'Normal')
)

class babyDetails(models.Model):
    body_color = models.CharField(max_length = 64)
    sex = models.CharField(choices=GENDER_CHOICES, max_length=128)
    delivery_time = models.CharField(max_length = 64)
    hospital_name = models.CharField(choices = HOSPITAL_NAMES, max_length = 64)
    blood_group = models.CharField(max_length = 64)
    weight = models.CharField(max_length = 64)
    handicap = models.CharField(choices = YES_NO,max_length = 64)
    aids = models.CharField(choices = YES_NO, max_length = 64)
    doctor_name = models.CharField(max_length = 64)
    case_type = models.CharField(choices = CASE_TYPE, max_length = 64)
