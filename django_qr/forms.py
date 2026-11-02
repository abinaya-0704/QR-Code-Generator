from django import forms



class QRCodeForm(forms.Form):
    restaruant_name=forms.CharField(
        max_length=50,
        label='Restaruant Name',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter restaruant name',
        })
        )
    url=forms.URLField(
        max_length=200,
        label='Menu URL',
        widget=forms.URLInput(attrs={
            'class':'form-control',
            'placeholder': 'Enter the URL your online menu',

        })
        )

