from django.forms.models import BaseModelFormSet, modelformset_factory
from oscar.apps.basket.formsets import BaseBasketLineFormSet as CoreBaseBasketLineFormSet,\
BaseSavedLineFormSet as CoreBaseSavedLineFormSet
from oscar.core.loading import get_classes, get_model
from .forms import BasketLineForm, SavedLineForm

Line = get_model('basket', 'line')

BasketLineFormSet = modelformset_factory(
    Line, form=BasketLineForm, formset=CoreBaseBasketLineFormSet, extra=0,
    can_delete=True)

SavedLineFormSet = modelformset_factory(Line, form=SavedLineForm,
                                        formset=CoreBaseSavedLineFormSet, extra=0,
                                        can_delete=True)