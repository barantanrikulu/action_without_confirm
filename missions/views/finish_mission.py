from missions.models import Mission
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages


def finish_mission(request, id):
    mission = get_object_or_404(Mission, id=id)
    if mission.finished:
        mission.finished = False
        mission.save()
        messages.success(request, 'Mission UN-Finished.')

    else:
        mission.finished = True
        mission.save()

        messages.success(request, 'Mission Finished.')

    return redirect('/')
