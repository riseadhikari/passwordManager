from django import forms
from django.forms import ModelForm
from .models import User, Credential

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username']

	def __init__(self, *args, **kwargs):

		super(UserForm, self).__init__(*args, **kwargs)

		placeholder = iter(['Your Username Here'])

		for name, field in self.fields.items():
			
			field.widget.attrs.update({"class":"rm-outline form-control form-control-md border-top-0 border-left-0 border-right-0",
								
								"id":"username",
								"autocomplete":"off",
								'aria-autocomplete':"both",
								"aria-haspopup":"false",
								"autocapitalize":"off",
								"autocorrect":"off",
								"autofocus":"",
								"spellcheck":"false",'placeholder':next(placeholder)})


class CredentialForm(ModelForm):
	class Meta:
		model = Credential
		fields = ['service','username','email','password']

	def __init__(self, *args, **kwargs):

		super(CredentialForm, self).__init__(*args, **kwargs)

		placeholder = iter(['Service Here','Username Here','Email Here','Password Here'])

		for name, field in self.fields.items():
			
			field.widget.attrs.update({"class":"rm-outline form-control form-control-md border-top-0 border-left-0 border-right-0",
								
								"id":str(name),
								"autocomplete":"off",
								'aria-autocomplete':"both",
								"aria-haspopup":"false",
								"autocapitalize":"off",
								"autocorrect":"off",
								"autofocus":"",
								"spellcheck":"false",'placeholder':next(placeholder)})




