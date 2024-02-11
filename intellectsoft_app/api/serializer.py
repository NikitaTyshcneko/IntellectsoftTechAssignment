from rest_framework import serializers
from intellectsoft_app.models import Client, Request


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    processed_by = serializers.SerializerMethodField()

    def get_processed_by(self, obj):
        if obj.processed_by:
            return {
                'first_name': obj.processed_by.first_name,
                'last_name': obj.processed_by.last_name,
            }
        return None

    def get_client(self, obj):
        return {
            'first_name': obj.client.first_name,
            'last_name': obj.client.last_name,
        }

    class Meta:
        model = Request
        fields = '__all__'
