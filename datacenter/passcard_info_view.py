from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def duration_and_check(duration):
    time_in_storage = int(round(duration))
    hours = time_in_storage // 3600
    minutes = (time_in_storage % 3600) // 60
    if hours > 1 and minutes > 1:
        return f"{hours} ч {minutes} м", "ДА"
    return f"{hours} ч {minutes} м", "НЕТ"


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)
    storage_user = Visit.objects.filter(passcard=passcard[0])
    user_visits = []
    for visit in storage_user:
        this_passcard_visits = {
                'entered_at': visit.entered_at,
                'duration': duration_and_check(visit.get_duration())[0],
                'is_strange': duration_and_check(visit.get_duration())[1],
            }
        user_visits.append(this_passcard_visits)

    context = {
        'passcard': passcard[0],
        'this_passcard_visits': user_visits
    }
    return render(request, 'passcard_info.html', context)
