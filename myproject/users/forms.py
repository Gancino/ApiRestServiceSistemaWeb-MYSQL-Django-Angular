from django import forms
from users.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'avatar',
            'work',
            'direccion',
            'telefono',
            'empresa',
            'descripcion'
        )