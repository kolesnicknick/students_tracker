from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from groups.models import Group


def groups(request):
    qset = Group.objects.all()
    return render(request, 'group_list.html', context={'group_list': qset})


def generate_group(request):
    group = Group.gen_group()
    return HttpResponse(f'{group.get_info()}')


def group_add(request):
    from groups.forms import GroupAddForm

    if request.method == 'POST':
        form = GroupAddForm(request.POST)
        if form.is_valid():
            form.save()
            from django.urls import reverse
            return HttpResponseRedirect(reverse('group-list'))
    else:
        form = GroupAddForm()

    return render(request,
                  'group_add.html',
                  context={'form': form})


def group_edit(request, pk):
    from groups.forms import GroupAddForm

    try:
        group = Group.objects.get(id=pk)
    except group.DoesNotExist:
        return HttpResponseNotFound(f'Find other group, group with id: {pk} is not found')

    if request.method == 'POST':
        form = GroupAddForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            from django.urls import reverse
            return HttpResponseRedirect(reverse(groups()))
    else:
        form = GroupAddForm(instance=group)

    return render(request, 'group_edit.html', context={'form': form, 'pk': pk})


def group_delete(request, pk):
    Group.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse('group-list'))
