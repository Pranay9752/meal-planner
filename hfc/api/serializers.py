from rest_framework import serializers

class CaloriesSerializer(serializers.Serializer):

    calories = serializers.IntegerField(max_value=10000,min_value=1)