from django.db import models

# Create your models here.
from django.db import models
MODIFICATION_TITLE = (
    ('ENLARGE', 'ENLARGE'),
    ('SHORTEN', 'SHORTEN'),
)

from oscar.apps.basket.abstract_models import AbstractBasket, AbstractLineAttribute

class AddModification(models.Model):
    modification_title = models.CharField(max_length=250, choices=MODIFICATION_TITLE)
    modification_price = models.CharField(max_length=250, null=True)
    modification_comment = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.modification_title

class LineAttribute(AbstractLineAttribute):
    add_modification=models.ForeignKey(to=AddModification, on_delete=models.CASCADE, null=True, blank=True, related_name='modification')

from oscar.apps.basket.models import *
