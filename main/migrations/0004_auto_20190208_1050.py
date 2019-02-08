# Generated by Django 2.1.5 on 2019-02-08 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190205_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='q_format',
            field=models.CharField(choices=[('mcq', 'MCQ'), ('openended', 'OPENENDED'), ('radio', 'RADIO')], max_length=450, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='email_date',
            field=models.DateField(default=datetime.date(2019, 2, 8)),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='post_date',
            field=models.DateField(default=datetime.date(2019, 2, 8)),
        ),
    ]
