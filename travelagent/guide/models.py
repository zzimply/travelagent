from django.db import models


class Country(models.Model):

    class Meta:
        app_label = 'guide'

    name = models.CharField(max_length=100)

#class Question(models.Model):

#    class Meta:
#        app_label = 'guide'

#    text = models.CharField(max_length=4096)
