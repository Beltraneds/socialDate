from django.db import models

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Interes(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50, blank=True, null=True)
    correo = models.EmailField(max_length=80, unique=True)
    contrasena = models.CharField(max_length=18)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/')
    fecha_nacimiento = models.DateField()
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"

class Chat(models.Model):
    nombre_chat = models.CharField(max_length=30)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_chat

class Foto(models.Model):
    imagen = models.ImageField(upload_to='fotos/')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Like(models.Model):
    cantidad = models.IntegerField()

class Match(models.Model):
    descripcion = models.CharField(max_length=80)
    cantidad = models.IntegerField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

class UsuarioInteres(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    interes = models.ForeignKey(Interes, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'interes')

class UsuarioLike(models.Model):
    like = models.ForeignKey(Like, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('like', 'usuario')

class UsuarioMatch(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'match')