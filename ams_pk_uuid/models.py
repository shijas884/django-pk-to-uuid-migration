from django.db import models
# step -> import uuid
import uuid

# “first step 1 migration normal added the pk field migration”
class AppointmentUser(models.Model):
    appointmentUser_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_uuid = models.UUIDField(null=True)        # 👈 NEW FIELD STEP -> 1
    name = models.CharField(max_length=100)
    discription = models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_uuid = models.UUIDField(null=True)  # 👈 ADD Step -> 3
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Slot(models.Model):
    STATUS_CHOICES = (
        ("booked", "Booked"),
        ("open", "Open"),
    )
    slot_id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    date = models.DateField(null=True)
    user = models.ForeignKey(AppointmentUser, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="open")
