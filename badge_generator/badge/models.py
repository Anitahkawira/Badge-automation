from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=50)
    other_names = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    id_no = models.CharField(max_length=20, unique=True)
    photo = models.FileField(upload_to='photos')

    def __str__ (self):
        return self.other_names + ' ' + self.surname