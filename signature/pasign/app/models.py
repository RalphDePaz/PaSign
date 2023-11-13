from tkinter import Image
from django.db import models

class UserData(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=15)
    email = models.EmailField()
    signature_type = models.CharField(max_length=50)
    
    # New field for file uploads
    signature_files = models.FileField(upload_to='user_signatures/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
