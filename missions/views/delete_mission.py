from missions.models import Mission
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages


def delete_mission(request, id):
    mission = get_object_or_404(Mission, id=id)
    mission.delete()
    messages.success(request, 'Comment deleted succesfully.')
    return redirect('/')
