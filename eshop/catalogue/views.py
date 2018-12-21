from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from oscar.apps.basket.views import BasketView as CoreBasketView, BasketAddView as CoreBasketAddView

from extra_views import ModelFormSetView
from oscar.apps.basket.signals import (
    basket_addition, voucher_addition, voucher_removal)
from oscar.core import ajax
from oscar.core.loading import get_class, get_classes, get_model
from oscar.core.utils import redirect_to_referrer, safe_referrer

(BasketLineForm, AddToBasketForm, BasketVoucherForm, SavedLineForm) = get_classes(
    'basket.forms', ('BasketLineForm', 'AddToBasketForm',
                     'BasketVoucherForm', 'SavedLineForm'))
BasketLineFormSet, SavedLineFormSet = get_classes(
    'basket.formsets', ('BasketLineFormSet', 'SavedLineFormSet'))

class BasketView(ModelFormSetView):
    model = get_model('basket', 'Line')
    basket_model = get_model('basket', 'Basket')
    formset_class = BasketLineFormSet
    form_class = BasketLineForm
    factory_kwargs = {
        'extra': 0,
        'can_delete': True
    }
    template_name = 'basket/basket.html'