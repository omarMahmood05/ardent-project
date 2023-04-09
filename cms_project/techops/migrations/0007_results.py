# Generated by Django 4.1 on 2022-08-30 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techops', '0006_delete_results'),
    ]

    operations = [
        migrations.CreateModel(
            name='results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('subject_name', models.CharField(max_length=50)),
                ('subject_grade', models.CharField(max_length=50)),
                ('subject_marks', models.IntegerField()),
            ],
        ),
    ]