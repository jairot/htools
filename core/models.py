from django.db import models


class Hackaton(models.Model):
    user = models.ForeignKey('auth.User',related_name='hackatones')
    nombre = models.CharField(max_length=50)
    background_img = models.URLField(default='media/default_background.png')
    hora_inicio = models.DateTimeField()
    hora_final = models.DateTimeField()
    tw_hashtag = models.CharField(max_length=20)
    nombre_hackdash = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    udpated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nombre