from django.db import models
from django.contrib.auth.models import User

class Klasa(models.Model):
    nazwa = models.CharField("nazwa klasy", max_length=3, default="")
    rok_matury = models.IntegerField("rok matury", default=0)
    rok_naboru = models.IntegerField("rok naboru", default=0)

    class Meta:
        verbose_name_plural = 'klasy'
        ordering = ['rok_naboru']

    def __str__(self):
        return self.nazwa + f" ({self.rok_naboru})"

class Absolwent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    klasa = models.ForeignKey(Klasa, on_delete=models.SET_NULL, blank=True, null=True, related_name="uczniowie")

    class Meta:
        verbose_name_plural = 'absolwenci'

    def __str__(self):
        return self.user.get_full_name()

class Dokument(models.Model):
    opis = models.CharField(max_length=255, unique=True)
    plik = models.FileField(upload_to='dokumenty/')
    data_d = models.DateTimeField("dodano", auto_now_add=True)

    class Meta:
        verbose_name_plural = 'dokumenty'

    def __str__(self):
        return self.opis
