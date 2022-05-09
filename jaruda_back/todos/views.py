from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .models import Todo
from rest_framework.views import APIView
from .serializers import TodoSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class TodoListApi(APIView):
    def get(self, request):
        queryset = Todo.objects.all()
        # print(queryset)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)



@csrf_exempt
def get_todo(request, pk):
    try: 
        obj = Todo.objects.filter(pk=pk).first()
    except Exception as ex:
        #serializer = TodoSerializer(obj)
        return JsonResponse(ex.args[0], status=400)
    else:
        serializer = TodoSerializer(obj)
        return JsonResponse(serializer.data, status=200)