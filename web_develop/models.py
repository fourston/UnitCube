from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    project_url = models.CharField(max_length=250)
    sort_index = models.IntegerField(default=100)
    preview_img = models.FileField(upload_to = 'pictures%Y/%m/%d')

    def __str__(self):
        return self.title


class Advantage(models.Model):
    title = models.CharField(max_length=50)
    sort_index = models.IntegerField(default=100)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    sort_index = models.IntegerField(default=100)
    adv_list = models.ForeignKey(Advantage) #лист преимуществ лучше будет переделать на choices, как тут https://github.com/fourston/django-rest-formpatterns/blob/master/formpatterns/models.py

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField
    sort_index = models.IntegerField(default=100)

    def __init__(self):
        self.description
