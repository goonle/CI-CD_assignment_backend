from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Note.models import Note
from Note.serializers import NoteSerializer


# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

class NoteCreateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        user = request.user
        title = request.data.get('title')
        content = request.data.get('content')

        if not title or not content:
            return Response({"error": "Title and content are required"}, status=status.HTTP_400_BAD_REQUEST)

        note = Note.objects.create(user=user, title=title, content=content)
        return Response({"message": "Note created successfully", "note_id": note.id}, status=status.HTTP_201_CREATED)


class NoteListView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]