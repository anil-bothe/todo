from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)


    """ form : radio btn"""
    # GENDER_BY = (
    #     (0, "Female"),
    #     (1, "male")
    # )

    # gender = models.IntegerField(choices=GENDER_BY)
