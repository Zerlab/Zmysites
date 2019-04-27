# Generated by Django 2.2 on 2019-04-26 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookInfo',
            fields=[
                ('ranking', models.CharField(default='', max_length=3, primary_key=True, serialize=False)),
                ('bookname', models.CharField(default='', max_length=32)),
                ('infos', models.CharField(default='', max_length=50)),
                ('appraise', models.CharField(default='', max_length=32)),
                ('peoplenum', models.CharField(default='', max_length=32)),
                ('content', models.CharField(default='', max_length=100)),
            ],
        ),
    ]