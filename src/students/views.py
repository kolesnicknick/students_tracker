from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import render

from students.models import Student


def students(request):
    queryset = Student.objects.all()
    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(first_name__istartswith=fn)
    return render(request, 'student_list.html', context={'students_list': queryset})


def generate_student(request):
    student = Student.generate_student()
    return HttpResponse(f'{student.get_info()}')


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
                  'teacher_add.html',
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
                  context={'form': form, 'pk': pk})
