from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
        else:
            return HttpResponse('not register')

    args = {}
    args.update(csrf(request))
    args['form']  = UserCreationForm()

    return render(request, 'analysis/register.html', args)
