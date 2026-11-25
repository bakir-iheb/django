from django.db import models

# Create your models here.
class Status(models.TextChoices):
    PENDING = 'Pending' ,'Pending'
    CONFIRMED = 'Confirmed' , 'Confirmed'
    CANCELLED = 'Cancelled' ,'Cancelled'

class Appointment(models.Model):
    reason = models.TextField()
    #prescription = models.TextField()
    status = models.CharField(max_length=20,choices=Status.choices,default=Status.PENDING)
    duration = models.IntegerField(30)
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doctor= models.ForeignKey('AccountApp.Doctor', on_delete=models.CASCADE,null=True, blank=True)
    patient= models.ForeignKey('AccountApp.Patient', on_delete=models.CASCADE,null=True, blank=True)