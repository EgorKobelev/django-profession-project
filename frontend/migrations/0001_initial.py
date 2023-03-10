# Generated by Django 4.1.5 on 2023-01-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryAndVacanciesPerYearsProfessionTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('average_salary', models.IntegerField()),
                ('average_salary_profession', models.IntegerField()),
                ('vacancies_count', models.IntegerField()),
                ('vacancies_count_profession', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SalaryPerCityTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SalaryPerYearsGraphics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photo')),
            ],
        ),
        migrations.CreateModel(
            name='VacanciesPerCityGraphics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photo')),
            ],
        ),
        migrations.CreateModel(
            name='VacanciesPerCityTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('vacancy_rate', models.IntegerField()),
            ],
        ),
    ]
