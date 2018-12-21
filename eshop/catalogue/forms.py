from django import forms
from django.conf import settings
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _

from oscar.forms import widgets
from oscar.apps.basket.forms import BasketLineForm as CoreBasketLineForm,\
SavedLineForm as CoreSavedLineForm, AddToBasketForm as CoreAddToBasketForm

from .models import AddModification
from oscar.core.loading import get_model, get_classes

Line = get_model('basket', 'line')
Basket = get_model('basket', 'basket')
Product = get_model('catalogue', 'product')

class BasketLineForm(CoreBasketLineForm):
    class AddModificationForm(CoreBasketLineForm.Meta):
        model = AddModification
        fields = ['modification_title', 'modification_price', 'modification_comment']

class SavedLineForm(CoreSavedLineForm):
    class AddModificationForm(CoreSavedLineForm.Meta):
        model = AddModification
        fields = ['modification_title', 'modification_price', 'modification_comment']
