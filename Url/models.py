"""    <!--=====================================
       devopled by fabin ziyad
       github: https://github.com/fabin-ziyad
    ==========================================-->"""
from django.db import models
# Create your models here.
class Url(models.Model):
    link=models.CharField(max_length=10000)
    uuid=models.CharField(max_length=10)
    