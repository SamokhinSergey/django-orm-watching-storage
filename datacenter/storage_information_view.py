from django.shortcuts import render
from django.utils.timezone import localtime


def duration_and_check(duration):
    time_in_storage = int(round(duration))
    hours = time_in_storage // 3600
    minutes = (time_in_storage % 3600) // 60
    if hours > 1 and minutes > 1:
        return f"{hours} ч {minutes} м", "ДА"
    return f"{hours} ч {minutes} м", "НЕТ"


def storage_information_view(request):
    from datacenter.models import Visit  # noqa: E402
    active_visitors = Visit.objects.filter(leaved_at__isnull=True)
    visitors_in_storage = []
    for index, active_visitor in enumerate(active_visitors):
        entried_msk = localtime(active_visitors[index].entered_at)
        visitor_in_sorage = {
            'who_entered': active_visitors[index].passcard,
            'entered_at': entried_msk,
            'duration':
                duration_and_check(active_visitors[index].get_duration())[0],
            'is_strange':
                duration_and_check(active_visitors[index].get_duration())[1],
        }
        visitors_in_storage.append(visitor_in_sorage)
    context = {
        'non_closed_visits': visitors_in_storage,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
