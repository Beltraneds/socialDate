# Generated by Django 5.0.6 on 2024-06-04 03:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_chat', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_genero', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Interes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_interes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipousu', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=80)),
                ('cantidad', models.IntegerField(default=0)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='socialdate.chat')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(blank=True, max_length=50, null=True)),
                ('correo', models.EmailField(max_length=80, unique=True)),
                ('contrasena', models.CharField(max_length=18)),
                ('foto_perfil', models.ImageField(upload_to='fotos_perfil/')),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='socialdate.genero')),
                ('tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='socialdate.tipousuario')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='socialdate.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='fotos/')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='socialdate.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='socialdate.usuario'),
        ),
        migrations.CreateModel(
            name='UsuarioInteres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_intereses', to='socialdate.interes')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_intereses', to='socialdate.usuario')),
            ],
            options={
                'unique_together': {('usuario', 'interes')},
            },
        ),
        migrations.CreateModel(
            name='UsuarioLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_likes', to='socialdate.like')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_likes', to='socialdate.usuario')),
            ],
            options={
                'unique_together': {('like', 'usuario')},
            },
        ),
        migrations.CreateModel(
            name='UsuarioMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_matches', to='socialdate.match')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_matches', to='socialdate.usuario')),
            ],
            options={
                'unique_together': {('usuario', 'match')},
            },
        ),
    ]
