from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User


# Create your models here.
class Patient_data(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_id = models.CharField(
        primary_key=True, max_length=100, default='1701775')
    hist_image = models.FileField(upload_to=None, max_length=254, blank=True)
    diagnosis_result = models.CharField(max_length=100)
    pathologist = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return super().__str__()

class Assess(models.Model):
    patient_id = models.ForeignKey(Patient_data, on_delete=models.CASCADE)
    menopause = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    density = models.CharField(max_length=100)
    bmi = models.CharField(max_length=100)
    agefirst = models.CharField(max_length=100)
    nrelbc = models.CharField(max_length=100)
    brstproc = models.CharField(max_length=100)
    lastmamm = models.CharField(max_length=100)
    surgmeno = models.CharField(max_length=100)
    hrt = models.CharField(max_length=100)
    invasive = models.CharField(max_length=100)
    risk_result = models.CharField(max_length=100)
    pathologist = models.ForeignKey(User, on_delete=models.CASCADE, null=True)