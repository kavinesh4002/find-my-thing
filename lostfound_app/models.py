from django.db import models

class LostItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, blank=True, null=True)  # Make optional
    date_reported = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name

class FoundItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, blank=True, null=True)  # Make optional
    date_reported = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name
