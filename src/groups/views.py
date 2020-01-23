from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from groups.models import Group


def groups(request):
    queryset = Group.objects.all()
    fn = request.GET.get('q')
    if fn:
        q1 = queryset.filter(group_name__istartswith=fn)
        q2 = queryset.filter(senior__first_name__istartswith=fn)
        q3 = queryset.filter(curator__first_name__istartswith=fn)
        queryset = q1.union(q2).union(q3)
    return render(request, 'group_list.html', context={'group_list': queryset})


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
            return HttpResponseRedirect(reverse('group-list'))
    else:
        form = GroupAddForm(instance=group)

    return render(request, 'group_edit.html', context={'form': form, 'pk': pk})


def group_delete(request, pk):
    Group.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse('group-list'))
