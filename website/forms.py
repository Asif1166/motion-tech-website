from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg shadow-sm',
            'placeholder': 'Your Name'
        }),
        error_messages={'required': 'Name is required.'}
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg shadow-sm',
            'placeholder': 'Your Email'
        }),
        error_messages={
            'required': 'Email is required.',
            'invalid': 'Invalid email address.'
        }
    )
    
    subject = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg shadow-sm',
            'placeholder': 'Subject'
        }),
        error_messages={'required': 'Subject is required.'}
    )
    
    message = forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control form-control-lg shadow-sm',
            'placeholder': 'Your Message',
            'rows': 5
        }),
        error_messages={'required': 'Message is required.'}
    )

