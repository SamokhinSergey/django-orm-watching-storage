def format_duration(duration):
    time_in_storage = int(round(duration))
    hours = time_in_storage // 3600
    minutes = (time_in_storage % 3600) // 60
    return {'hours': hours, 'minutes': minutes}


def check_suspicious(hours, minutes):
    suspicious = hours > 1 and minutes > 1
    return suspicious

