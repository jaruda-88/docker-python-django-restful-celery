from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .serializers import TodoSerializer, CreateTodoSerializer
from .schemas import (
    extn_create_todo,
    extn_read_todos,
    extn_edit_todo,
    extn_delete_todo
)
from .tasks import print_todo


# Create your views here.
class TodoList(APIView):
    @extn_read_todos
    def get(self, request):
        ''' GET 할일 목록 '''
        try:
            pk = request.GET.get('id')
            if int(pk) == 0:
                todos = Todo.objects.all()
                serializer = TodoSerializer(todos, many=True)
                for todo in todos:
                    print_todo.delay(todo.task)
                result = serializer.data
            else:
                todos = Todo.objects.filter(pk=pk).first()
                serializer = TodoSerializer(todos)
            result = [] if not todos else serializer.data   
        except Exception as ex:
            return Response(ex.args[0], status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(result)

    
    @extn_create_todo
    def post(self, request):    
        ''' POST 할일 등록 '''
        try:
            serializer = CreateTodoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                raise Exception(serializer.errors)
        except Exception as ex:
            return Response(ex.args[0], status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data)


    @extn_edit_todo
    def put(self, request):
        ''' PUT 할일 수정 '''
        try:
            data = request.data
            pk = data.get('id', 0)
            target = Todo.objects.filter(pk=pk).first()

            if not target:
                raise Exception('Not found')

            serializer = TodoSerializer(target, data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                raise Exception(serializer.errors)
        except Exception as ex:
            return Response(ex.args[0], status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Ok')

    
    @extn_delete_todo
    def delete(self, request):
        ''' DELETE 할일 삭제 '''
        try:
            pk = request.GET.get('id')
            target = Todo.objects.filter(pk=pk)
            if not target:
                raise Exception('Not found')
            target.delete()
        except Exception as ex:
            return Response(ex.args[0], status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('OK')



# sample 1
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse, JsonResponse
# @csrf_exempt
# def get_todo(request, pk):
#     try: 
#         obj = Todo.objects.filter(pk=pk).first()
#     except Exception as ex:
#         #serializer = TodoSerializer(obj)
#         return JsonResponse(ex.args[0], status=400)
#     else:
#         serializer = TodoSerializer(obj)
#         return JsonResponse(serializer.data, status=200)
# sample 2
# from rest_framework.decorators import api_view
# @api_view(['GET', 'DELETE'])
# def get_task(request, pk):
#     ''' GET path 할일/DELETE path 삭제 '''
#     try:
#         target = Todo.objects.filter(pk=pk).first()

#         if request.method == 'GET':
#             serializer = TodoSerializer(target)

#             result = [] if not target else serializer.data
#         elif request.method == 'DELETE':
#             target.delete()
#             result = 'Ok'
#         else:
#             raise Exception('method error')
#     except target.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     except Exception as ex:
#         return Response(ex.args[0], status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response(result)