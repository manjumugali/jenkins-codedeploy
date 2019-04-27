from django.db import models


class registerUser(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname + ' ' + self.lastname