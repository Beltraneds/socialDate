# Generated by Django 5.0.6 on 2024-06-04 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialdate', '0002_alter_usuario_contrasena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='socialdate.tipousuario'),
        ),
    ]
