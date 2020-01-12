from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from .models import Student


def students(request):
    # Student.objects.all
    pass


def generate_student(request):
    pass


def students_add(request):
    from .forms import StudentsAddForm

    if request.method == 'POST':
        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            from django.urls import reverse
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm()

    return render(request,
                  'student_add.html',
                  context={'form': form})


def students_edit(request, pk):
    from .forms import StudentsAddForm
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponseNotFound(f'Student with id {pk} not found')

    if request.method == 'POST':
        form = StudentsAddForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            from django.urls import reverse
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm(instance=student)

    return render(request,
                  'student_edit.html',
                  context={'form': form})
