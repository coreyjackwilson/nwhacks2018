# Generated by Django 2.0.1 on 2018-01-14 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20180114_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='user',
        ),
        migrations.AlterField(
            model_name='event',
            name='child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Camera'),
        ),
        migrations.DeleteModel(
            name='Child',
        ),
    ]
