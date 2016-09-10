from django import forms            
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm      
from .models import Gamer, Developer, Game
from django.core import mail
from hashlib import md5

class RegistrationForm(UserCreationForm):
    username = forms.CharField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(required = False, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required = False, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    developer = forms.BooleanField(label="Register as developer", required = False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),required = True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),required = True)

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username', 'password1', 'password2',]

    def save(self,commit = True):   
        user = super(RegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            print('saving user')
            user.is_active = False
            user.save()
            if self.cleaned_data['developer']:
                developer = Developer(user=user)
                developer.save()
            gamer = Gamer(user=user)
            gamer.save()

            secret_key = '6cd118b1432bf22942d93d784cd17084' # pitää muutaa http://payments.webcourse.niksula.hut.fi/key/
            checksumstr = "username={}&email={}&token={}".format(user.username, user.email, secret_key)
            m = md5(checksumstr.encode('ascii'))
            checksum = m.hexdigest()
            link = "http://localhost:8000/verify?&username={}&email={}&&checksum={}".format(user.username, user.email, checksum)
            with mail.get_connection() as connection:
                    mail.EmailMessage("Verify", link, "skeletor@skeletor.fi", [user.email],
                                                  connection=connection).send()


        return user

class PaymentForm(forms.Form):
    pid = forms.CharField(widget = forms.HiddenInput())
    sid = forms.CharField(widget = forms.HiddenInput())
    success_url = forms.URLField(widget = forms.HiddenInput())
    cancel_url = forms.URLField(widget = forms.HiddenInput())
    error_url = forms.URLField(widget = forms.HiddenInput())
    checksum = forms.CharField(widget = forms.HiddenInput())
    amount = forms.FloatField(widget = forms.HiddenInput())
    
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'description', 'publisher', 'genre', 'source', 'price']


