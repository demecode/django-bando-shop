from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    # quantity allows user to select quantity between 1 and 20
    # the typechoice field with coerce ensure input is converted to integer
    # if override is False then this means a quantity needs to be added to ana existing quantity in the cart
    # if true then the existing quantity with be overriden
    # hiddeninput widget to hide field from user
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label=_('Quantity'))
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
