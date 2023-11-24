from django.urls import path
from lottery.api.views import LotteryListAPIView, LotteryCreateAPIView, LotteryUpdateAPIView, LotteryWinnerAPIView

app_name = "lottery"
urlpatterns = [
    path('list/', LotteryListAPIView.as_view(), name='list'),
    path('create/', LotteryCreateAPIView.as_view(), name='create'),
    path('update/<pk>/', LotteryUpdateAPIView.as_view(), name='update'),
    path('winner/<pk>/', LotteryWinnerAPIView.as_view(), name='winner'),
]