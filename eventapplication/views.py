from django.shortcuts import render
from .models import Participants


# Create your views here.
def home(request):
    context = {}
    return render(request, 'eventapplication/home.html', context)

def registration(request):
    context = {}
    if request.method == 'POST':
        p1 = Participants()
        p1.username = request.POST.get('username', '-')
        p1.email = request.POST.get('email', '-')
        p1.phone = request.POST.get('phone', '-')
        p1.institution = request.POST.get('institution', '-')

        if len(Participants.objects.all()) > 15:
            return render(request, 'eventapplication/failed.html', context)
        else:
            p1.save()
            return render(request, 'eventapplication/success.html', context)

    if request.method == 'GET':
        context['username'] = ''
        context['email'] = ''
        context['phone'] = ''
        

    return render(request, 'eventapplication/registration.html', context)


def listofparticipants(request):
    context = {}
    context['participants'] = Participants.objects.all()
    return render(request, 'eventapplication/listofparticipants.html', context)



