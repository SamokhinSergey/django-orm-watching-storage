def duration_format(duration):
    time_in_storage = int(round(duration))
    hours = time_in_storage // 3600
    minutes = (time_in_storage % 3600) // 60
    return {'hours': hours, 'minutes': minutes}


def duration_check(hours, minutes):
    if hours > 1 and minutes > 1:
        return True
    return False
