from rest_framework.pagination import PageNumberPagination


class PaginateBy20(PageNumberPagination):
    page_size = 20