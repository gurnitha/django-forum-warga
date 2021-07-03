# apps/boards/forms.py

# Django modules
from django import forms

# Django locals
from apps.boards.models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message'] # message is new field added

"""
This is our first form. It’s a ModelForm associated 
with the Topic model. The subject in the fields list 
inside the Meta class is referring to the subject 
field in the Topic class. 

Now observe that we are defining an extra field named message. 
This refers to the message in the Post we want to save.
"""        