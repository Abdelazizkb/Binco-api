# Generated by Django 3.2.5 on 2021-08-27 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trashCan', '0005_auto_20210827_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trashcan',
            name='position',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='position', to='trashCan.localisation'),
        ),
    ]
