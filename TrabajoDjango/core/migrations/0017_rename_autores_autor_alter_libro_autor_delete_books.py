# Generated by Django 4.2.11 on 2024-04-14 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_rename_autor_autores_alter_books_imagenn'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Autores',
            new_name='Autor',
        ),
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='books',
        ),
    ]