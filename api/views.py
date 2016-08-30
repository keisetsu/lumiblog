from django.http import Http404

from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from api.models import Entry
from api.serializers import EntrySerializer


class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
