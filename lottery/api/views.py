from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from lottery.api.serializers import LotterySerializer, LotteryCreateUpdateSerializer, LotteryWinnerSerializer
from lottery.models import Lottery


class LotteryListAPIView(ListAPIView):
    queryset = Lottery.objects.all()
    serializer_class = LotterySerializer
    filter_backends = [SearchFilter]
    search_fields = ['id']


class LotteryCreateAPIView(CreateAPIView):
    queryset = Lottery.objects.all()
    serializer_class = LotteryCreateUpdateSerializer
    permission_classes =[IsAuthenticated]

class LotteryUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Lottery.objects.all()
    serializer_class = LotteryCreateUpdateSerializer
    permission_classes =[IsAuthenticated]
    lookup_field = 'pk'

class LotteryWinnerAPIView(RetrieveUpdateAPIView):
    queryset = Lottery.objects.all()
    serializer_class = LotteryWinnerSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'





