from django.db import models


class Hackaton(models.Model):
    user = models.ForeignKey('auth.User',related_name='hackatones')  # Nombre de usuario
    nombre = models.CharField(max_length=50)  # Nombre de hackaton
    background_img = models.ImageField(default='/assets/img/bg.png', upload_to='backgrounds')  # Imagen a usar como background
    hora_inicio = models.DateTimeField()  # Hora de inicio de hackaton. El datetime se saca con el request.
    hora_final = models.DateTimeField()  # Hora en la que finaliza la hackaton
    tw_hashtag = models.CharField(max_length=20)  # Hashtag de los twits que se muestran
    tw_time = models.IntegerField()  # Tiempo en segundos antes de mostrar el siguiente twit
    page_time = models.IntegerField()  # Tiempo en segundos antes de cambiar a la siguiente pagina (timer, twits, proyectos)
    nombre_hackdash = models.CharField(max_length=20)  # Nombre del proyecto en HackDash
    created = models.DateTimeField(auto_now_add=True)
    udpated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nombre
