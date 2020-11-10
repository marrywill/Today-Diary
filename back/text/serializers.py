from rest_framework import serializers

# from accounts.serializers import UserSerializer
from .models import *
from post.serializers import EmotionSerializer

class WordCloudReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordCloudReport
        fields = ('word', 'count', 'emotion')


class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = ('id', 'score', 'emotion', 'date', 'user_emotion')
        # depth = 1

class UserSelectEmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = ('user_emotion',)

class WeeklyDateSerializer(serializers.Serializer):
    start = serializers.DateField()
    end = serializers.DateField()
    today = serializers.DateField()


class MonthlyDateSerializer(serializers.Serializer):
    year = serializers.CharField()
    month = serializers.CharField()


class SelectEmotionSerializer(serializers.Serializer):
    # post_id = serializers.IntegerField()
    emotion = serializers.IntegerField()