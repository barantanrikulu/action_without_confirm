from django.shortcuts import redirect, render
from django.template.defaultfilters import title
from missions.models import Mission
from missions.forms import AddMissionModelForm


def homepage(request):
    add_mission_form = AddMissionModelForm
    missions = Mission.objects.all().order_by('-id')
    if request.method == "POST":
        add_mission_form = add_mission_form(request.POST)
        if add_mission_form.is_valid():
            add_mission_form.save()
            return redirect('/')
    context = {
        'add_mission_form': add_mission_form,
        'missions': missions
    }
    return render(request, 'homepage.html', context=context)
