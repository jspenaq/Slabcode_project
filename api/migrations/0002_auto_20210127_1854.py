# Generated by Django 3.1.5 on 2021-01-27 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('ENP', 'En Proceso'), ('FIN', 'Finalizado')], default='ENP', max_length=3),
        ),
    ]