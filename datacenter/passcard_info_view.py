from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.time_tools import duration_format, duration_check


def passcard_info_view(request, passcode):
    passcards = Passcard.objects.filter(passcode=passcode)
    visits_serialized = Visit.objects.filter(passcard=passcards[0])
    user_visits = []
    for visit in visits_serialized:
        duration_time = duration_format(visit.get_duration())
        duration_hours = duration_time['hours']
        duration_minutes = duration_time['minutes']
        this_passcard_visits = {
                'entered_at': visit.entered_at,
                'duration': f"{duration_hours }ч {duration_minutes}м",
                'is_strange': duration_check(duration_hours, duration_minutes),
            }
        user_visits.append(this_passcard_visits)

    context = {
        'passcard': passcards[0],
        'this_passcard_visits': user_visits
    }
    return render(request, 'passcard_info.html', context)
