# Generated by Django 4.2.11 on 2024-04-14 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0018_delete_autor_remove_libro_categoria_libro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='categoriaLibro/')),
            ],
        ),
    ]
