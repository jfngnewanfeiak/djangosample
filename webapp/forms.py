from django import forms
from webapp.models import Post
from webapp.models import Schedule
class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class BS4ScheduleForm(forms.ModelForm):
    '''Bootstrap model form...'''

    class Meta:
        model = Schedule
        fields = ('summary', 'description', 'start_time', 'end_time')
        widgets = {
            'summary':forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'start_time': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'end_time': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }
    
    def clean_end_time(self):
        start_time = self.cleaned_data['start_time']
        end_time = self.cleaned_data['end_time']
        if end_time <= start_time:
            raise forms.ValidationError(
                'end_time must be later than start_time...'
            )
        return end_time