# Generated by Django 3.2.4 on 2021-10-15 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='lists',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='tasks.list'),
        ),
    ]
