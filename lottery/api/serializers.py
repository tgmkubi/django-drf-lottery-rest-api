from rest_framework import serializers

from competitor.models import Competitor
from lottery.models import Lottery

class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competitor
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'is_active',
            'lottery'
        ]

class LotterySerializer(serializers.ModelSerializer):

    # Competitor modelinde tanımladığımız related_name="competitors_of_lotteries" buraya erişmemizi sağladı.
    competitors_of_lotteries = CompetitorSerializer(many=True, read_only=True)

    class Meta:
        model = Lottery
        fields = [
            'id',
            'lottery_name',
            'winner',
            'competitors_of_lotteries'   # Competitor modelinde tanımladığımız related_name="competitors_of_lotteries" buraya erişmemizi sağladı.
        ]

class LotteryCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lottery
        fields = [
            'lottery_name',
        ]

    def validate(self, attrs):

        lotteryFromDatabase =Lottery.objects.filter(lottery_name=self.instance.lottery_name).first() # all metodu yazılabilirdi. for loop ile müşteriden gelen veri ile veritabı içinde arama yapılabilirdi.
        lotteryNameFromCustomer = attrs['lottery_name']

        # lotteryNameFromCustomer = self.context['request'].data.get('lottery_name')


        if str(lotteryFromDatabase) == lotteryNameFromCustomer:
            raise serializers.ValidationError("This lottery already exists")

        return attrs

    # Bu motodlar Serializer taradından otomatik olarak çalıştırılır, ilave işlem yapılmayacaksa tanımlamamıza gerek yok.
    # Ancak mail gönderme vs gibi işlemlerde işimize yarayabilir.
    def create(self, validated_data):
        return Lottery.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.lottery_name = validated_data.get('lottery_name', instance.lottery_name)
        instance.save()
        return instance


class LotteryWinnerSerializer(serializers.ModelSerializer):
    competitors_of_lotteries = CompetitorSerializer(many=True, read_only=True)
    class Meta:
        model = Lottery
        fields = [
            'id',
            'lottery_name',
            'winner',
            'select_winner',
            'competitors_of_lotteries'
        ]

        read_only_fields = ['lottery_name', 'winner']

