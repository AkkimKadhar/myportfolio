from django.db import models

class data(models.Model):
    name=models.CharField(max_length=50,default="")
    mail=models.EmailField(max_length=50,default="")
    message=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.name
