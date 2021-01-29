from django.db import models

# Create your models here.
class Employ(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=20)
    eemail=models.EmailField()
    econtact=models.CharField(max_length=15)
    elocn=models.CharField(max_length=15)
    class Meta:
        db_table="emp"