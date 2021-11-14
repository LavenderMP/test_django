from django.db import models


# Create your models here.


class SignIn(models.Model):
    error = models.BooleanField()
    messages = models.CharField(max_length=256, blank=True, default='')
    value = models.JSONField()
    question = models.BooleanField()
    twoFA = models.BooleanField()
    # TODO: ADD forginekey with post model associated with
    def __str__(self):
        return self.value


class TwoFA(models.Model):
    twoFaType = models.IntegerField()
    gaActivated = models.IntegerField()

    def __str__(self):
        return self.twoFaType, self.gaActivated


class Post(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    ip = models.CharField(max_length=40)

    # TODO: ADD DATETIME
    def __str__(self):
        return self.username