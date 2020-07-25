import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from .service import get_submit_streak
from .models import Submit


class ServiceTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='jacob', email='jacob@mail.ru', password='top_secret')

        Submit(user=user, date=timezone.datetime(year=2020, month=7, day=23, hour=16, minute=53)).save()
        Submit(user=user, date=timezone.datetime(year=2020, month=7, day=24, hour=19, minute=20)).save()
        # Submit(user=user, date=datetime.datetime(year=2020, month=7, day=22)).save()
        # Submit(user=user, date=datetime.datetime(year=2020, month=7, day=23)).save()

    def test_streak(self):
        user = User.objects.get(username='jacob')
        print(get_submit_streak(user))