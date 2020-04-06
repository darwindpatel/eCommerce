from django import forms
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
#User = get_user_model
class ContactForm(forms.Form):
	full_name = forms.CharField(
					widget=forms.TextInput(
								attrs={
										"class" : "form-control", 
										"placeholder" : "Your full name"
									}
									)
					)
	email = forms.EmailField(widget=forms.EmailInput(
								attrs={
										"class" : "form-control", 
										"placeholder" : "Your email"
									}
									)
					)
	content = forms.CharField(
					widget=forms.Textarea(
								attrs={
										"class": "form-control",
										"placeholder" : "Your Message"
									}
									)
					)

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if not "gmail.com" in email:
			raise forms.ValidationError("Email has to be gmail.com")
		return email






























