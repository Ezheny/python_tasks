from datetime import date

def get_days_to_new_year():
    today = date.today()
    new_year = date((today.year + 1), 1, 1)
    time_to_newyear = abs(new_year - today)
    return time_to_newyear.days

