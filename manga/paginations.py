from rest_framework.pagination import PageNumberPagination


class MangaPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 1000
    page_query_param = "page_size"
