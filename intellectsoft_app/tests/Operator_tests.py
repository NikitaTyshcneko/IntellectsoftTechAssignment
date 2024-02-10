from django.test import TestCase
from intellectsoft_app.models import Operator
import pytest


class OperatorModelTestCase(TestCase):
    fixtures = ['operators.json']

    def test_operator_str_representation(self):
        operator = Operator.objects.get(pk=1)
        self.assertEqual(str(operator), "Joe Tribbiani")

    def test_operator_fields(self):
        operator = Operator.objects.get(pk=1)
        self.assertEqual(operator.first_name, "Joe")
        self.assertEqual(operator.last_name, "Tribbiani")

    def test_operator_count(self):
        self.assertEqual(Operator.objects.count(), 2)


pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class OperatorCRUDTestCase(TestCase):
    pytestmark = pytest.mark.django_db

    def test_create_operator(self):
        operator_data = {
            'first_name': 'Joe',
            'last_name': 'Tribbiani'
        }
        operator = Operator.objects.create(**operator_data)
        self.assertEqual(operator.first_name, 'Joe')
        self.assertEqual(operator.last_name, 'Tribbiani')

    def test_update_operator(self):
        """Test updating an Operator instance."""
        operator = Operator.objects.create(first_name='Joe', last_name='Tribbiani')
        operator.last_name = 'Smith'
        operator.save()
        updated_operator = Operator.objects.get(pk=operator.pk)
        self.assertEqual(updated_operator.last_name, 'Smith')

    def test_delete_operator(self):
        """Test deleting an Operator instance."""
        operator = Operator.objects.create(first_name='Joe', last_name='Tribbiani')
        operator_pk = operator.pk
        operator.delete()
        with self.assertRaises(Operator.DoesNotExist):
            Operator.objects.get(pk=operator_pk)