# Generated by Django 2.2.12 on 2020-12-24 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memo_text', models.CharField(max_length=200)),
                ('length', models.IntegerField(default=0)),
            ],
        ),
    ]
