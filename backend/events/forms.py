from django import forms
from .models import Event, Comment

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
