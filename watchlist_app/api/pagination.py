from rest_framework.pagination import PageNumberPagination

class WatchListPagination(PageNumberPagination):
    
    page_size=5
    page_query_param='p' # use of this is that instead of ?page=2 we can use ?p=2
    # max_page_size=10