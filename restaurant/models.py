from django.db import models

# Create your models here.

class Booking(models.Model):
    #Id_Booking = models.IntegerField(11)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(6)
    BookingDate = models.DateTimeField()

    def __str__(self) -> str:
        return self.Name


class Menu(models.Model):
    #Id_Menu = models.IntegerField(5)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Inventory= models.IntegerField(5)

    def __str__(self) -> str:
        return self.Title
    
