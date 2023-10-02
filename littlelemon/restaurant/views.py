from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

def index(request):
    return render(request,'index.html',{})

class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer # Aceasta este sintaxa pentru serializare atunci cand folosesc Model Serializer.
    #Daca folosesc functii de vizualizare va trebuie ca atunci cand instantiez un obiect, acesta va avea sintaxa: serializer_class = ClasaSerializare(queryset,many=True) 

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer 


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated] 


