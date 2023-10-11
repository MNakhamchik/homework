from rest_framework import serializers
from users.models import Answer
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['title', 'description']


class TicketResponseSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()

    class Meta:
        model = Answer
        fields = ['sender', 'content']


class TicketStatusSerializer(serializers.ModelSerializer):
    status = serializers.CharField(help_text='Статус тикета')

    class Meta:
        model = Ticket
        fields = ['status']

