from django.forms import ModelForm
from .models import Profile


class  ProfileCreationForm(ModelForm) :
    class meta :
        model = Profile
        fields = ['image', 'nickname', 'message']
