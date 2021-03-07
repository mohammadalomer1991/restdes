from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    #user_id= models.IntegerField(max_length=4,default=1)
    anger_perc= models.CharField(max_length=30)
  
