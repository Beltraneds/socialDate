from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class Genero(models.Model):
    nombre_genero = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_genero

class Interes(models.Model):
    nombre_interes = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_interes

class TipoUsuario(models.Model):
    nombre_tipousu = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_tipousu

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50, blank=True, null=True)
    correo = models.EmailField(max_length=80, unique=True)
    contrasena = models.CharField(max_length=128)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/')
    fecha_nacimiento = models.DateField()
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, related_name='usuarios', null=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='usuarios')

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"

class Chat(models.Model):
    nombre_chat = models.CharField(max_length=30)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='chats')

    def __str__(self):
        return self.nombre_chat

class Foto(models.Model):
    imagen = models.ImageField(upload_to='fotos/')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='fotos')

class Like(models.Model):
    cantidad = models.IntegerField(default=0)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='likes')

class Match(models.Model):
    descripcion = models.CharField(max_length=80)
    cantidad = models.IntegerField(default=0)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='matches')

class UsuarioInteres(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario_intereses')
    interes = models.ForeignKey(Interes, on_delete=models.CASCADE, related_name='usuario_intereses')

    class Meta:
        unique_together = ('usuario', 'interes')

class UsuarioLike(models.Model):
    like = models.ForeignKey(Like, on_delete=models.CASCADE, related_name='usuario_likes')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario_likes')

    class Meta:
        unique_together = ('like', 'usuario')

class UsuarioMatch(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario_matches')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='usuario_matches')

    class Meta:
        unique_together = ('usuario', 'match')