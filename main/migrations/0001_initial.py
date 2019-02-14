# Generated by Django 2.1.7 on 2019-02-14 15:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.CharField(max_length=5000000)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=45000)),
                ('q_type', models.CharField(choices=[('prepos', 'PREPOS'), ('experiment', 'EXPERIMENT'), ('placebo', 'PLACEBO'), ('control', 'CONTROL')], max_length=450, null=True)),
                ('q_format', models.CharField(choices=[('mcq', 'MCQ'), ('openended', 'OPENENDED'), ('radio', 'RADIO')], max_length=450, null=True)),
                ('q_category', models.IntegerField(null=True)),
                ('choice1', models.CharField(default='wsr', max_length=4500, null=True)),
                ('choice2', models.CharField(default='wsr', max_length=4500, null=True)),
                ('choice3', models.CharField(default='wsr', max_length=4500, null=True)),
                ('choice4', models.CharField(default='wsr', max_length=4500, null=True)),
                ('choice5', models.CharField(default='wsr', max_length=4500, null=True)),
                ('choice6', models.CharField(default='wsr', max_length=4500, null=True)),
                ('choice7', models.CharField(default='wsr', max_length=4500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('education_level', models.CharField(max_length=100)),
                ('contactno', models.PositiveIntegerField()),
                ('group', models.CharField(choices=[('prepos', 'PREPOS'), ('experiment', 'EXPERIMENT'), ('placebo', 'PLACEBO'), ('control', 'CONTROL')], max_length=450, null=True)),
                ('state', models.CharField(default='Bihar', max_length=100)),
                ('city', models.CharField(max_length=100, null=True)),
                ('category', models.IntegerField(default=-1)),
                ('status', models.IntegerField(default=1)),
                ('email_date', models.DateField(default=datetime.date(2019, 2, 14))),
                ('q_no', models.IntegerField(default=1)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='q_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='userdata_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Userdata'),
        ),
    ]
