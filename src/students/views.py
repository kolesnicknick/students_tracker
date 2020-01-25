import logging

from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from students.models import Student


def students(request):
    queryset = Student.objects.all().select_related('groups')
    fn = request.GET.get('q')
    if fn:
        q1 = queryset.filter(first_name__istartswith=fn)
        q2 = queryset.filter(last_name__istartswith=fn)
        q3 = queryset.filter(emails__istartswith=fn)
        queryset = q1.union(q2).union(q3)
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
            return HttpResponseRedirect(reverse('students-list'))
    else:
        form = StudentsAddForm(instance=student)

    return render(request,
                  'student_edit.html',
                  context={'form': form, 'pk': pk})


def students_delete(request, pk):
    Student.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse('students-list'))


def email(request):
    from students.forms import ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            logging.info(f"USER CONTACTED WITH MAIL: {form.cleaned_data['email']} "
                         f"AND SUBJECT: {form.cleaned_data['subject']}")
            form.save()
            return HttpResponseRedirect(reverse('students-list'))
    else:
        form = ContactForm()

    return render(request,
                  'contact.html',
                  context={'form': form})
