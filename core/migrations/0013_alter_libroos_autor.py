# Generated by Django 4.2.11 on 2024-04-14 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_rename_libros_libroos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libroos',
            name='autor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='aut', to='core.autor'),
        ),
    ]
