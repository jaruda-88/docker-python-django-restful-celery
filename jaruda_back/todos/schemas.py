from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from .serializers import *


post_todo = extend_schema( 
    summary='post task',
    tags=['todos'],
    # description='Todos',
    request=PostTodoSerializer,
    responses={200: TodoSerializer},
    # parameters=[
    #     OpenApiParameter(name='artist', description='Filter by artist', required=False, type=str),
    # ],
)


get_todos = extend_schema( 
    summary='todolist',
    tags=['todos'],
    responses={200: TodoSerializer},
)
