# Generated by Django 4.2.11 on 2024-04-14 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_libro_autor_libro_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='juego',
            name='categoria_juego',
        ),
        migrations.DeleteModel(
            name='Categoria_Juego',
        ),
        migrations.DeleteModel(
            name='Juego',
        ),
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='autores', to='core.autor'),
        ),
    ]
