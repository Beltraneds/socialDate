from django import forms
from .models import Usuario, Genero, Interes, TipoUsuario
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm

class RegistroUsuarioForm(forms.ModelForm):
    confirmar_contrasena = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'correo', 'contrasena', 'fecha_nacimiento', 'genero', 'foto_perfil']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        contrasena = cleaned_data.get("contrasena")
        confirmar_contrasena = cleaned_data.get("confirmar_contrasena")
        
        if contrasena != confirmar_contrasena:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        
        cleaned_data['contrasena'] = make_password(contrasena)  # Hash la contraseña
        
        return cleaned_data

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.id_tipo_usuario = TipoUsuario.objects.get(nombre_tipousu='Normal')  # Asignar "Normal" por defecto
        if commit:
            usuario.save()
        return usuario
    
class SeleccionInteresesForm(forms.Form):
    intereses = forms.ModelMultipleChoiceField(
        queryset=Interes.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        help_text="Selecciona entre 1 y 5 intereses."
    )

    def clean_intereses(self):
        intereses = self.cleaned_data.get('intereses')
        if len(intereses) < 1 or len(intereses) > 5:
            raise forms.ValidationError("Debes seleccionar entre 1 y 5 intereses.")
        return intereses
    
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Correo'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contraseña'})