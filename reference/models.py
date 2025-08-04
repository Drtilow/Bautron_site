from django.db import models

class Reference(models.Model):
    TYP_STAVBY = [
        ('novostavba', 'Novostavba'),
        ('rekonstrukce', 'Rekonstrukce'),
        ('drevostavba', 'Dřevostavba'),
        ('jine', 'Jiné'),
    ]

    nazev = models.CharField(max_length=100)
    popis = models.TextField()
    typ = models.CharField(max_length=20, choices=TYP_STAVBY, default='jine')
    obrazek = models.ImageField(upload_to='reference/', blank=True, null=True)
    datum_realizace = models.DateField()
    publikovano = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nazev
