from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .serializers import TodoSerializer, PostTodoSerializer
from .schemas import *


# Create your views here.
@api_view(['GET', 'DELETE'])
def get_task(request, pk):
    try:
        todos = Todo.objects.filter(pk=pk).first()

        if request.method == 'GET':
            serializer = TodoSerializer(todos)

            result = [] if not todos else serializer.data
        elif request.method == 'DELETE':
            todos.delete()
            result = 'Ok'
        else:
            raise Exception('method error')
    except todos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return Response(ex.args[0], status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(result)



class TodoList(APIView):
    @get_todos
    def get(self, request):
        try:
            todos = Todo.objects.all()
            serializer = TodoSerializer(todos, many=True)
        except todos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
        except Exception as ex:
            return Response(ex.args[0], status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data)

    
    @post_todo
    def post(self, request):    
        try:
            serializer = PostTodoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                raise Exception(serializer.errors)
        except Exception as ex:
            return Response(ex.args[0], status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data)


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