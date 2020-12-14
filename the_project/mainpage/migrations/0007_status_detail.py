# Generated by Django 3.1 on 2020-12-14 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_delete_status_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status_detail',
            fields=[
                ('status_id', models.IntegerField(default='SOME CATEGORY', primary_key=True, serialize=False)),
                ('detail', models.CharField(default='', max_length=10)),
                ('projectlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.project')),
            ],
        ),
    ]
