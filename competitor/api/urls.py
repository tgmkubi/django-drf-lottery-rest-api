from django.urls import path
from competitor.api.views import CompetitorCreateAPIView, CompetitorListAPIView, CompetitorUpdateAPIView


app_name="competitor"
urlpatterns = [
    path('list/', CompetitorListAPIView.as_view(), name='list'),
    path('register/', CompetitorCreateAPIView.as_view(), name='register'),
    path('update/<pk>', CompetitorUpdateAPIView.as_view(), name='update')
]