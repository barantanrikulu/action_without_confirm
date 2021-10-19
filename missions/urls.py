from missions.views import homepage, delete_mission, finish_mission
from django.urls import path

app_name = 'missions'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('delete/<int:id>/', delete_mission, name='delete_mission'),
    path('finish/<int:id>/', finish_mission, name='finish_mission'),

]
