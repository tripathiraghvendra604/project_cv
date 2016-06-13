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
    #print request.POST
    form = EducationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        data_dict = dict(request.POST)

        # for twelve data saving
        #print data_dict
        inter = {}
        # marks will be a dict whose key will be subject name
        # and value will be a list whose first value is marks and second value
        # is the maximum marks in the subject
        marks = {}

        twelve_board = data_dict.get('Board12')
        twelve_percent = data_dict.get('Percent12')
        twelve_file = str(form.cleaned_data.get('File12'))
        twelve_marks_list = data_dict.get('MarksScored12[]')
        twelve_subjects_list = data_dict.get('Subject12[]')
        twelve_max_marks_list = data_dict.get('MaximumMarks12[]')
        inter['board'] = twelve_board
        inter['percent'] = twelve_percent
        for i in range(len(twelve_subjects_list)):   # for marks dict
            marks[twelve_subjects_list[i]] = [twelve_marks_list[i], twelve_max_marks_list[i]]

        inter['board'] = twelve_board
        inter['percent'] = twelve_percent
        inter['marks'] = marks

        t= json.dumps(inter)
        print t
        print type(t)



        # MarksScored12 = list(request.POST.get('MarksScored12[]'))
        # Subject12 = list(request.POST.get('Subject12[]'))
        # print str(MarksScored12) + ' is marks scored in 12'
        # print str(Subject12) + ' is Subject12 in 12'
        #print form.cleaned_data
        # for high school data saving
        high = {}
        ten_board = form.cleaned_data.get('ten_board')
        ten_percent = form.cleaned_data.get('ten_percent')
        ten_file = (form.cleaned_data.get('ten_file'))
        high['board'] = ten_board
        high['percent'] = ten_percent
        #high['doc'] = ten_file
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
                               intermediate= t, intermediate_doc=twelve_file,
                               graduation = g, graduation_doc=g_file,
                               post_graduation=p, post_graduation_doc=pg_file)
        data.save()
        print 'data saved'

    else:
        print 'invalid form'

    context = {
        'form': form,
        'g' : g,
        'pg': pg,
    }

    return render(request, 'educational.html', context)