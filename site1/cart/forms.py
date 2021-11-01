from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label="Колличество", widget=forms.TextInput(attrs={'id': 'quantityInp', 'value': 1, 'pattern': '[0-9]*'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)