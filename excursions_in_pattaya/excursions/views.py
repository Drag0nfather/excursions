from django.shortcuts import render
from .models import Excursion


def excursion_list(request):
    excursions = Excursion.objects.all()
    return render(request, 'main_page.html', {'excursions': excursions})
