from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.time_tools import format_duration, check_suspicious
from datacenter.models import Visit


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    active_visits_serialized = []
    for index, active_visitor in enumerate(active_visits):
        entried_msk = localtime(active_visits[index].entered_at)
        duration_time = format_duration(active_visits[index].get_duration())
        duration_hours = duration_time['hours']
        duration_minutes = duration_time['minutes']
        visitor_in_sorage = {
            'who_entered': active_visits [index].passcard,
            'entered_at': entried_msk,
            'duration': f"{duration_hours}ч {duration_minutes}м",
            'is_strange': check_suspicious(duration_hours, duration_minutes),
        }
        active_visits_serialized.append(visitor_in_sorage)
    context = {
        'non_closed_visits': active_visits_serialized,
    }
    return render(request, 'storage_information.html', context)
