from django.db import models
#meaning of makemigrations and migrate here below:
# makemigrations- create changes and store in a file   
# migrate- apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()


    