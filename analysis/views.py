from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from .forms import UserInfoForm
from django.http import Http404
from django.shortcuts import redirect, render
from .forms import EducationForm
from .models import PostGraduateCourse, UnderGraduateCourse, EducationalInfo
import json
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

        return HttpResponse('data saved')
    else:
        print 'home data not saved'

    context = {
        'form': form,
    }
    return render(request, 'home.html', context)

def education(request):

    # g and p are for choices for graduate
    # and post graduate courses

    g = UnderGraduateCourse.objects.all()
    pg = PostGraduateCourse.objects.all()

    form = EducationForm(request.POST or None, request.FILES or None)
    if form.is_valid():

        # for high school data saving
        high = {}
        ten_board = form.cleaned_data.get('ten_board')
        ten_percent = form.cleaned_data.get('ten_percent')
        ten_file = form.cleaned_data.get('ten_file')
        high['board'] = ten_board
        high['percent'] = ten_percent
        h = json.dumps(high)

        graduate = {}
        g_board = form.cleaned_data.get('g_board')
        g_percent = form.cleaned_data.get('g_percent')
        g_file = form.cleaned_data.get('g_file')
        graduate['board'] = g_board
        graduate['percent'] = g_percent
        g = json.dumps(graduate)

        p_graduate = {}
        pg_board = form.cleaned_data.get('pg_board')
        pg_percent = form.cleaned_data.get('pg_percent')
        pg_file = form.cleaned_data.get('pg_file')
        p_graduate['board'] = pg_board
        p_graduate['percent'] = pg_percent
        p = json.dumps(p_graduate)

        user = request.user
        # saving data in database
        data = EducationalInfo(user=user,
                               high_school=h, high_school_doc=ten_file,
                               graduation = g, graduation_doc=g_file,
                               post_graduation=p, post_graduation_doc=pg_file)
        data.save()
        print 'data saved'

    context = {
        'form': form,
        'g' : g,
        'pg': pg,
    }
    return render(request, 'educational.html', context)