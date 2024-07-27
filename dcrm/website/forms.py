from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'forms-control','placeholder':'Email Address'}))
    first_name = forms.CharField(label="",max_length="100",widget=forms.TextInput(attrs={'class':'forms-control','placeholder':'First Name'}))
    last_name = forms.CharField(label="",max_length="100",widget=forms.TextInput(attrs={'class':'forms-control','placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

        def __init__(self,*args,**kwargs):
            super(SignupForm,self).__init__(*args,**kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'User Name'
            self.fields['username'].label = ''
            self.fields['username'].help_text = '<span class = "form-text text-muted" <small>Required. 150 characters or fewer. </small></span>'
            
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password can\'t have lesser than 8 characters.</li></ul>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<span class="form-text text-muted small"><small>Your password should match as given before,for verification</small></span>'