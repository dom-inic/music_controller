from rest_framework.views import APIView
from rest_framework.response import Response  
from django.shortcuts import get_object_or_404
from rest_framework import generics 
from . models import Question, Choice 
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer

# class PollList(APIView):
#     def get(self, request):
#         polls = Question.objects.all()[:20]
#         data = PollSerializer(polls, many=True).data 
#         return Response(data)

# class PollDetail(APIView):
#     def get (self, request, pk):
#         poll = get_object_or_404(Question, pk=pk)
#         data = PollSerializer(poll).data 
#         return Response(data) 


class PollList(generics.ListCreateAPIView):
    queryset = Question.objects.all() 
    serializer_class = PollSerializer

class PollDetail(generics.RetrieveDestroyAPIView):
    queryset  = Question.objects.all()
    serializer_class = PollSerializer 

class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer 

class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer