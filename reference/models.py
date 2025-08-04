from django.db import models

class Reference(models.Model):
    TYPY = [
        ('RD', 'Rodinný dům'),
        ('BYT', 'Bytová jednotka'),
        ('KOM', 'Komerční stavba'),
    ]

    nazev = models.CharField(max_length=100)
    popis = models.TextField()
    typ = models.CharField(max_length=4, choices=TYPY)
    obrazek = models.ImageField(upload_to='reference/', null=True, blank=True)

    def __str__(self):
        return self.nazev
