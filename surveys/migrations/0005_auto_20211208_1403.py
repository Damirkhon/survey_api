# Generated by Django 2.2.10 on 2021-12-08 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0004_auto_20211208_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='surveys.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_type',
            field=models.IntegerField(choices=[('RADIOBUTTON', 'Radiobutton'), ('MULTIPLE', 'Multiple'), ('TEXT', 'Text')], default='RADIOBUTTON'),
        ),
    ]
