# Generated by Django 4.2.11 on 2024-04-14 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_rename_autores_autor_alter_libro_autor_delete_books'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='categoria_libro',
        ),
        migrations.DeleteModel(
            name='Categoria_Libro',
        ),
        migrations.DeleteModel(
            name='Libro',
        ),
    ]
