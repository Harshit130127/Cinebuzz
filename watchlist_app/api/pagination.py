from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class WatchListPagination(PageNumberPagination):
    
    
    page_size=5
    # page_query_param='p' # use of this is that instead of ?page=2 we can use ?p=2
    max_page_size=10 # if user tries to set a very high page size, it will be capped at this value
    page_size_query_param='size' # to allow user to set the page size dynamically
    # last_user_page_strings='last'  # to access the last page using ?page=end
     
     
class WatchListLOPagination(LimitOffsetPagination):
    
    default_limit=5
    max_limit=10
    limit_query_param='limit'  # to allow user to set the limit dynamically
    offset_query_param='offset'  # to allow user to set the offset dynamically
    
    
    
class WatchListCPagination(CursorPagination):
    
    page_size=5
    ordering='created'  # based on which field the pagination will be done
    cursor_query_param='record'  # this is not for end user use, it's for internal use to keep track of the cursor position or the name of the query parameter for the cursor