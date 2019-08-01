from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class HostelProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional details
    hostel_Name = models.CharField(max_length=100, blank=True)
    manager_Email = models.EmailField(max_length=70, blank=True)
    contacts = models.CharField(max_length=50, blank=True)
    hostel_choice = [('G', 'Girls Hostel'), ('B', 'Boys Hostel')]
    hostelType = models.CharField(choices=hostel_choice, max_length=1, blank=True)
    room_choice = [('AC', 'Air Conditioned'), ('NAC', 'Non Air Conditioned'), ('B', 'Both')]
    roomType = models.CharField(choices=room_choice, max_length=3, blank=True)
    room_Occupancy = models.CharField(max_length=100, blank=True)
    mess_choice = [('A', 'Available'), ('NA', 'Not Available')]
    foodmess = models.CharField(choices=mess_choice, max_length=2, blank=True)
    wifi_choice = [('A', 'Available'), ('NA', 'Not Available')]
    wifi = models.CharField(choices=wifi_choice, max_length=2, blank=True)
    vacancy_choice = [('A', 'Available'), ('NA', 'Not Available')]
    vacancy = models.CharField(choices=vacancy_choice, max_length=2, blank=True)
    state = models.CharField(max_length=70, blank=True)
    city = models.CharField(max_length=70, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    monthly_Rent = models.IntegerField(null=True, blank=True)
    descriptions = models.TextField(default='', blank=True) 
     

    def __str__(self):
        return self.user.username


class HostelImage(models.Model):
    hostel = models.ForeignKey('hostels.HostelProfile', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='pictures/', blank=True)
    
    def __str__(self):
    	return self.hostel.hostel_name + " Image "