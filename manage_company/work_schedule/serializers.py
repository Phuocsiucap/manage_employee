from rest_framework import serializers
from .models import work_schedule

class work_scheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = work_schedule
        fields = [ 'employee_id', 'work_day', 'shift']
    