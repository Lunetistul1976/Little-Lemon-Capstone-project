from rest_framework import serializers
from .models import Menu,Booking
from django.contrib.auth.models import User


class MenuSerializer(serializers.ModelSerializer):
 class Meta:
  model = Menu
  fields = ['id','Title','Price','Inventory']

class BookingSerializer(serializers.ModelSerializer):
   class Meta:
     model = Booking
     fields = ['id','Name','No_of_guests','BookingDate']


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username','url','email','groups']     