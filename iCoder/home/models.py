from django.db import models

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    content = models.TextField()
    timeStamp = models.DateTimeField(default=models.DateTimeField)

    def __str__(self):
        return self.name