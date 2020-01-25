# Create your views here.
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import render

from teachers.models import Teacher


def teachers(request):
    queryset = Teacher.objects.all()
    fn = request.GET.get('q')
    if fn:
        q1 = queryset.filter(first_name__istartswith=fn)
        q2 = queryset.filter(last_name__istartswith=fn)
        q3 = queryset.filter(email__istartswith=fn)
        queryset = q1.union(q2).union(q3)
    return render(request, 'teacher_list.html', context={'teacher_list': queryset})


def generate_teacher(request):
    teacher = Teacher.gen_teacher()
    return HttpResponse(f'{teacher.get_info()}')


def teacher_add(request):
    from teachers.forms import TeacherAddForm

    if request.method == 'POST':
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            form.save()
            from django.urls import reverse
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeacherAddForm()

    return render(request,
                  'teacher_add.html',
                  context={'form': form})


def teachers_edit(request, pk):
    from teachers.forms import TeacherAddForm

    try:
        teacher = Teacher.objects.get(id=pk)
    except Teacher.DoesNotExist:
        return HttpResponseNotFound(f'Find other teacher, teacher with id: {pk} is not found')

    if request.method == 'POST':
        form = TeacherAddForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            from django.urls import reverse
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeacherAddForm(instance=teacher)

    return render(request, 'teacher_edit.html', context={'form': form, 'pk': pk})
