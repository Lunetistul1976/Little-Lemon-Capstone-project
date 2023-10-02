from django.db import models

class Menu(models.Model): # Numele tabelului creat in baza de date este nume-aplicatie_model
 Title = models.CharField(max_length=255)
 Price = models.DecimalField(max_digits=10,decimal_places=2)
 Inventory = models.SmallIntegerField()
 def __str__(self):
  return f'{self.Title} : {str(self.Price)}' # f este folosit atunci cand vrem sa folosim variabile in interiorul unor Strings
 # De fiecare data cand efectuez schimbari la nivelul modelului trebuie sa MIGREZ aceste schimbari

class Booking(models.Model):
 Name = models.CharField(max_length=255)
 No_of_guests = models.IntegerField()
 BookingDate = models.DateTimeField()
 def __str__(self):
  return self.Name

