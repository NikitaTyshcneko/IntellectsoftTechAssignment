from django.test import TestCase
import pytest
from intellectsoft_app.models import Client


class ClientModelTestCase(TestCase):
    fixtures = ["clients.json"]

    def test_client_str_representation(self):
        """Test the string representation of the Client model."""
        client = Client.objects.get(pk=1)
        self.assertEqual(str(client), "Ross Geller")

    def test_client_fields(self):
        """Test the fields of the Client model."""
        client = Client.objects.get(pk=1)
        self.assertEqual(client.first_name, "Ross")
        self.assertEqual(client.last_name, "Geller")
        self.assertEqual(client.phone, "123456789")

    def test_client_count(self):
        """Test the total count of clients."""
        self.assertEqual(Client.objects.count(), 2)


pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class ClientCRUDTestCase(TestCase):
    pytestmark = pytest.mark.django_db

    def test_create_client(self):
        client_data = {
            'first_name': 'Rachel',
            'last_name': 'Green',
            'phone': '123456789'
        }
        client = Client.objects.create(**client_data)
        self.assertEqual(client.first_name, 'Rachel')
        self.assertEqual(client.last_name, 'Green')
        self.assertEqual(client.phone, '123456789')

    def test_update_client(self):
        client = Client.objects.create(first_name='Rachel', last_name='Green', phone='123456789')
        client.phone = '987654321'
        client.save()
        updated_client = Client.objects.get(pk=client.pk)
        self.assertEqual(updated_client.phone, '987654321')

    def test_delete_client(self):
        client = Client.objects.create(first_name='Rachel', last_name='Green', phone='123456789')
        client_pk = client.pk
        client.delete()
        with self.assertRaises(Client.DoesNotExist):
            Client.objects.get(pk=client_pk)
