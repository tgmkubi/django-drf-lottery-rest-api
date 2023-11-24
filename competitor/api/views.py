from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView

from competitor.api.paginations import CompetitorAPIPagination
from competitor.api.serializers import CompetitorSerializer, CompetitorCreateSerializer, CompetitorUpdateSerializer
from competitor.models import Competitor


class CompetitorCreateAPIView(CreateAPIView):
    queryset = Competitor.objects.all()
    serializer_class = CompetitorCreateSerializer

class CompetitorListAPIView(ListAPIView):
    # queryset = Competitor.objects.all()
    serializer_class = CompetitorSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name']
    pagination_class = CompetitorAPIPagination

    # http://127.0.0.1:8000/api/competitor/list/?search=yavuz
    # http://127.0.0.1:8000/api/competitor/list/?order=-id
    # http://127.0.0.1:8000/api/competitor/list/?page=2

    def get_queryset(self):
        queryset = Competitor.objects.all()
        is_active = self.request.query_params.get('is_active')

        if is_active is not None:
            queryset = Competitor.objects.filter(is_active=is_active)
            # http://127.0.0.1:8000/api/competitor/list/?is_active=True

        return queryset

class CompetitorUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Competitor.objects.all()
    serializer_class = CompetitorUpdateSerializer
    lookup_field = 'pk'

    """
    def perform_update(self, serializer):
        super().perform_update(serializer)
        instance = serializer.instance
        instance.save()
    """

