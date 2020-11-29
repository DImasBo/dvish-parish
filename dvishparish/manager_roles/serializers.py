from rest_framework import serializers
from .models import ResultDaily

class ResultDailySerializer(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    KPI_id = serializers.IntegerField()
    KPI_result_amount = serializers.IntegerField()