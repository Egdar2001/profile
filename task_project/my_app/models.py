from django.db import models

# Create your models here.

class profile(models.Model):

    name=models.CharField(max_length=200)

    age=models.IntegerField()

    address=models.CharField(max_length=500)

    skill=models.CharField(max_length=100)

    def _str_(self):

        return '{}'.format(self.name)
    