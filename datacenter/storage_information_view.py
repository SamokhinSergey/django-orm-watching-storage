from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.time_tools import format_duration, check_suspicious
from datacenter.models import Visit


def storage_information_view(request):

    visits_serialized = Visit.objects.filter(leaved_at__isnull=True)
    visitors_in_storage = []
    for index, active_visitor in enumerate(visits_serialized):
        entried_msk = localtime(visits_serialized[index].entered_at)
        duration_time = format_duration(visits_serialized[index].get_duration())
        duration_hours = duration_time['hours']
        duration_minutes = duration_time['minutes']
        visitor_in_sorage = {
            'who_entered': visits_serialized[index].passcard,
            'entered_at': entried_msk,
            'duration': f"{duration_hours }ч {duration_minutes}м",
            'is_strange': check_suspicious(duration_hours, duration_minutes),
        }
        visitors_in_storage.append(visitor_in_sorage)
    context = {
        'non_closed_visits': visitors_in_storage,
    }
    return render(request, 'storage_information.html', context)
