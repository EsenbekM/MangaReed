from rest_framework.pagination import PageNumberPagination


class MangaPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 1000
    page_query_param = "page"


class TopMangaPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 20
    page_query_param = "page"


class GenrePagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_query_param = "page"
