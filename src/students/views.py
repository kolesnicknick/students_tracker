from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def students_add(request):
    from .forms import StudentsAddForm

    if request.method == 'POST':
        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')
    else:
        form = StudentsAddForm()

        
    return render(request,
                   'student_add.html',
                   context={'form': form})

    #return HttpResponse('ADD STUDENT')