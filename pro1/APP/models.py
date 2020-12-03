from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=10)
    address=models.CharField(max_length=50,null=False)
    number=models.IntegerField()
    comment=models.CharField(max_length=50,null=True)
    email=models.EmailField(null=False)


    def __str__(self):
        return self.name