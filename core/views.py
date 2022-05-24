from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .models import User, Book, Journal


from rest_framework.decorators import api_view
from rest_framework import permissions, status, generics
from .serializers import BookSerializer, JournalSerializer, UserSerializer, RegisterSerializer
from rest_framework import viewsets
# Create your views here.


class BooksViewSet(viewsets.ViewSet):


    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class JournaltViewSet(viewsets.ModelViewSet):


    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    parser_classes = [MultiPartParser]


    def create(self, request, *args, **kwargs):
        serializer = JournalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)



class RegisterApi(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
    
    
    
@api_view(['GET', 'POST', 'DELETE'])
def bookDetail(request, journalId):
    try:
        film = Book.objects.get(id=journalId)
    except Book.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = BookSerializer(film)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        film.delete()
        return Response({'message': 'deleted'}, status=404)
    
    
    
    
def journalDetail(request, journalId):
    try:
        journal = Journal.objects.get(id=journalId)
    except Book.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = JournalSerializer(journal)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = JournalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        journal.delete()
        return Response({'message': 'deleted'}, status=404)