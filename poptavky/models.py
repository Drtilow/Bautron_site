from django.db import models

class Poptavka(models.Model):
    jmeno = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.CharField(max_length=30)
    popis = models.TextField(help_text="Popište svůj požadavek nebo zakázku")
    odeslano = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.jmeno} – {self.email}"
