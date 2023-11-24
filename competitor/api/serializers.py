from rest_framework import serializers

from competitor.models import Competitor
from lottery.models import Lottery

class LotterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lottery
        fields = '__all__'

class CompetitorSerializer(serializers.ModelSerializer):
    lottery = LotterySerializer()
    class Meta:
        model = Competitor
        fields = [
            'id',
            'first_name',
            'last_name',
            'lottery',
            'email',
            'phone_number',
            'is_active'
        ]

class CompetitorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competitor
        fields = [
            'id',
            'first_name',
            'last_name',
            'lottery',
            'email',
            'phone_number'
        ]

class CompetitorUpdateSerializer(serializers.ModelSerializer):

    onePassword = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Competitor
        fields = [
            'first_name',
            'last_name',
            'lottery',
            'email',
            'phone_number',
            'is_active',
            'onePassword',
        ]

