from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

class suggetion(models.Model):
    date=models.DateField()
    sugg=models.CharField(max_length=100)
    sub=models.TextField()
    expl=models.TextField()
    image=models.ImageField(upload_to='picture')
