from rest_framework.pagination import PageNumberPagination


class CompetitorAPIPagination(PageNumberPagination):
    page_size = 3