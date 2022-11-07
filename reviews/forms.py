from django import forms

from .models import Review

# Django form

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=100, error_messages={
#                                 "required": "Your name must not be empty",
#                                 "max_length": "Please enter a shorted name"
#                                 })
#     review_text = forms.CharField(
#         label="Your feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)

# Django form model


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "user_name": "Your name",
            "feedback": "Your feedback",
            "rating": "Your rating"
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty",
                "max_length": "Please enter a shorted name"
            }
        }
