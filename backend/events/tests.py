from django.test import TestCase
from .models import Event

class EventModelTest(TestCase):
    def test_event_creation(self):
        event = Event.objects.create(
            title = 'TEST EVENT',
            description = 'THIS IS A TEST EVENT',
            data = '2021-01-01 12:00:00',
            location ='TEST LOCATION',
        )
        self.assertEqual(event.title, 'Test Event')