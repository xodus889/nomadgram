from django.db import models

# Create your models here.
class TimeStampModel(models.Model) :

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True) 

    class Meta :
        abstract = True


class Image(TimeStampModel) :

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()


class Commnet(TimeStampModel) :

    message = models.TextField()