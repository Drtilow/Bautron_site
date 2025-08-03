from django.db import models

class Poptavka(models.Model):
    jmeno = models.CharField(max_length=100)
    email = models.EmailField()
    predmet = models.CharField(max_length=200)
    zprava = models.TextField()
    vytvoreno = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.jmeno} – {self.predmet}"
