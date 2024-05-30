from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from todolist.models import todolist,dontu
from .serializer import listserializer,dontuserializer

# Create your views here.

@api_view(['GET'])
def abit(request):
    a={1:'abit'}
    return Response(a)

@api_view(['GET'])
def alllists(request):
    lists=todolist.objects.all()
    serializer=listserializer(lists,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getlists(request,id):
    lists=todolist.objects.get(id=id)
    serializer=listserializer(lists,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def alldontu(request):
    lists=dontu.objects.all()
    serializer=dontuserializer(lists,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getdontu(request,id):
    lists=dontu.objects.get(id=id)
    serializer=dontuserializer(lists,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def adddon(request):
    serializer=dontuserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["GET","PUT","DELETE"])
def donts(request,id):
    pro=dontu.objects.get(id=id)
    if request.method=="GET":
        serializer=dontuserializer(pro,many=False)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=dontuserializer(pro,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method=="DELETE":
        pro.delete()
        return Response('deleted')





