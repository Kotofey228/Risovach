import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from .service import get_submit_streak
from .models import Submit


class ServiceTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='jacob', email='jacob@mail.ru', password='top_secret')
        Submit(user=user, date=timezone.datetime(year=2020, month=7, day=15, hour=12)).save()
        Submit(user=user, date=timezone.datetime(year=2020, month=7, day=16, hour=12)).save()
        Submit(user=user, date=timezone.datetime(year=2020, month=7, day=17, hour=12)).save()
        Submit(user=user, date=timezone.datetime(year=2020, month=7, day=18, hour=12)).save()
        Submit(user=user, date=timezone.datetime(year=2020, month=7, day=19, hour=12)).save()
        Submit(user=user, date=timezone.datetime(year=2020, month=7, day=20, hour=12)).save()
        Submit(user=user, date=timezone.datetime(year=2020, month=7, day=21, hour=12)).save()
        Submit(user=user, date=timezone.datetime(year=2020, month=7, day=22, hour=12)).save()
        Submit(user=user, date=timezone.datetime(year=2020, month=7, day=23, hour=12)).save()
        # Submit(user=user, date=datetime.datetime(year=2020, month=7, day=22)).save()
        # Submit(user=user, date=datetime.datetime(year=2020, month=7, day=23)).save()

    def test_streak(self):
        user = User.objects.get(username='jacob')
        print(get_submit_streak(user))