# Generated by Django 4.2.11 on 2024-04-15 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_autor_nombre_alter_libro_autor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='categoria',
            new_name='categoria_Libro',
        ),
    ]