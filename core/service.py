import datetime

from django.utils import timezone

from .models import Submit


def get_submit_streak(user):
    submits = Submit.objects.filter(user=user).values_list('date', flat=True).order_by('-date')

    today = timezone.now()
    compare_date = today
    today_submitted = False
    day = 0

    if len(submits) == 0:
        return 1, today_submitted

    if submits[0].date() == today.date():
        today_submitted = True

    for date in submits:
        delta = compare_date - date

        if delta.days == 1:
            day += 1
        elif delta.days == 0:
            pass
        else:
            break

        compare_date = date

    day = day % 7
    return day + 1, today_submitted
