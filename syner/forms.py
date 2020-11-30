from django.forms import ModelForm
from backend.models import UserInfo


class SignupForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'

