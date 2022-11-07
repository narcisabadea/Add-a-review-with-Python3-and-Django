from django import forms


class ProfileForm(forms.Form):
    # using FileField
    # user_image = forms.FileField()

    # using ImageField
    user_image = forms.ImageField()
