import datetime


def format_viewing_time(viewing_time: str) -> str:
    hour, minute = map(int, viewing_time.split(':'))
    time_obj = datetime.time(hour=hour, minute=minute)
    return time_obj.isoformat(timespec='milliseconds') + 'Z'