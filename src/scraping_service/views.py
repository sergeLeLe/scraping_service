from django.shortcuts import render
import datetime


def home(request):
    # рандом данные для внесения их в шаблон
    date = datetime.datetime.now().date()
    name = 'Dave'
    _context = {
        'date': date,
        'name': name
    }  # в шаблон информация вносится с помощью словарей

    return render(request, 'home.html', _context)  # рендер запроса, 2 обязательных параметра - request, шаблон
    # страницы (.html). 3 параметр - словарь для внесения данных в шаблон
