from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from .forms import UserInfoForm
from django.http import Http404
from analysis.models import UserInfo

# Create your views here.

def home(request):
    if not request.user.is_authenticated():
        raise Http404
    form = UserInfoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print str(request.user.id) + 'is id of ' + str(request.user)
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # fname = form.cleaned_data.get('fname')
        # lname = form.cleaned_data.get('lname')
        # dob = form.cleaned_data.get('dob')
        # place_of_birth = form.cleaned_data.get('place_of_birth')
        # image = form.cleaned_data.get('image')
        # info = UserInfo(
        #     user = user,
        #     fname= fname,
        #     lname= lname,
        #     dob= dob,
        #     place_of_birth= place_of_birth,
        #     image= image
        # )
        # info.save()
        print 'data saved'

        return HttpResponse('data saved')

    context = {
        'form': form,
    }
    return render(request, 'home.html', context)