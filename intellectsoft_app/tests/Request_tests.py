import pytest
from django.test import TestCase
from intellectsoft_app.models import Request, Client


pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class RequestCRUDTestCase(TestCase):
    pytestmark = pytest.mark.django_db

    def setUp(self):
        # Create a client
        self.client = Client.objects.create(first_name='Chandler', last_name='Bing', phone='123456789')

    def test_create_request(self):
        request_data = {
            'client': self.client,
            'body': 'Sample request body',
            'status': 'Pending',
            'processed_by': None
        }
        request = Request.objects.create(**request_data)
        self.assertEqual(request.client, self.client)
        self.assertEqual(request.body, 'Sample request body')
        self.assertEqual(request.status, 'Pending')
        self.assertIsNone(request.processed_by)

    def test_update_request(self):
        request = Request.objects.create(client=self.client, body='Sample request body', status='Pending', processed_by=None)
        request.status = 'Completed'
        request.save()
        updated_request = Request.objects.get(pk=request.pk)
        self.assertEqual(updated_request.status, 'Completed')

    def test_delete_request(self):
        request = Request.objects.create(client=self.client, body='Sample request body', status='Pending', processed_by=None)
        request_pk = request.pk
        request.delete()
        with self.assertRaises(Request.DoesNotExist):
            Request.objects.get(pk=request_pk)
