from dataclasses import field, fields
from rest_framework import serializers

from calapp.models import Event
 
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id','event_name', 'start_time','end_time')
