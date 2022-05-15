from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.time_tools import format_duration, check_suspicious


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    visits = Visit.objects.filter(passcard=passcard)
    visits_serialized = []
    for visit in visits:
        duration_time = format_duration(visit.get_duration())
        duration_hours = duration_time['hours']
        duration_minutes = duration_time['minutes']
        this_passcard_visits = {
                'entered_at': visit.entered_at,
                'duration': f"{duration_hours }ч {duration_minutes}м",
                'is_strange': check_suspicious(duration_hours, duration_minutes),
            }
        visits_serialized.append(this_passcard_visits)

    context = {
        'passcard': passcard,
        'this_passcard_visits': visits_serialized
    }
    return render(request, 'passcard_info.html', context)
