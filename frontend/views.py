from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'frontend/index.html', {'title': "Frontend"})


def demand(request):
    demand_table_info = SalaryAndVacanciesPerYearsProfessionTable.objects.all()
    demand_graphic_info = SalaryPerYearsGraphics.objects.all()
    context = {
        'title': "Востребованность",
        "demand_table_info": demand_table_info,
        "demand_graphic_info": demand_graphic_info
    }
    return render(request, 'frontend/demand.html', context=context)


def geography(request):
    geography_vacancies_table_info = VacanciesPerCityTable.objects.all()
    geography_graphic_info = VacanciesPerCityGraphics.objects.all()
    geography_salary_table_info = SalaryPerCityTable.objects.all()
    context = {
        'title': "География",
        "geography_vacancies_table_info": geography_vacancies_table_info,
        "geography_graphic_info": geography_graphic_info,
        "geography_salary_table_info": geography_salary_table_info
    }
    return render(request, 'frontend/geography.html', context=context)


def skills(request):
    return render(request, 'frontend/skills.html', {'title': "Навыки"})


def vacancy(request):
    return render(request, 'frontend/vacancy.html', {'title': "Последние вакансии"})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
