# Generated by Django 3.2.11 on 2022-03-27 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wm', '0002_commonsubject'),
        ('accounts2', '0008_auto_20220117_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='common_subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wm.commonsubject'),
            preserve_default=False,
        ),
    ]
