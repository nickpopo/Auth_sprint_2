# Generated by Django 3.1 on 2021-03-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0026_removed_id_indexes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='age_limit',
            field=models.IntegerField(blank=True, null=True, verbose_name='Возрастной ценз'),
        ),
        migrations.AlterField(
            model_name='personrole',
            name='role',
            field=models.CharField(blank=True, choices=[('actor', 'актер'), ('director', 'режиссер'), ('scriptwriter', 'сценарист')], max_length=255, null=True, verbose_name='роль'),
        ),
    ]