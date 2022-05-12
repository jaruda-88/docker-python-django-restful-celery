from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from .serializers import (
    CreateTodoSerializer,
    TodoSerializer,
    FixTodoSerializer
)


extn_create_todo = extend_schema( 
    summary='post task',
    tags=['todos'],
    # description='Todos',
    request=CreateTodoSerializer,
    responses={200: TodoSerializer},
)


extn_read_todos = extend_schema( 
    summary='get todos',
    tags=['todos'],
    responses={200: TodoSerializer},
    parameters=[
        OpenApiParameter(name='id',
        description='task id(pk)', 
        required=True, 
        type=int,
        location=OpenApiParameter.QUERY,
        )
    ],
)


extn_edit_todo = extend_schema(
    summary='modify task',
    tags=['todos'],
    request=FixTodoSerializer,
    responses={200: 'Ok'},
)


extn_delete_todo = extend_schema(
    summary='delete task',
    tags=['todos'],
    responses={200: 'Ok'},
    parameters=[
        OpenApiParameter(name='id',
        description='task id(pk)', 
        required=True, 
        type=int,
        location=OpenApiParameter.QUERY,
        )
    ],
)
