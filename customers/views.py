from django.shortcuts import render
from categories.models import Sport

def Home(request):
    sports = Sport.objects.all()
    context={
        'Sport': sports
    }
    return render(request, 'customers/index.html', context)