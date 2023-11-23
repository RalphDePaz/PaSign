from django.db import models
import os

def get_user_signature_path(instance, filename):
    #Create the folder
    folder_name = f"Student {instance.student_id}"
    return os.path.join(folder_name, filename)

class UserData(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=15)
    email = models.EmailField()
    signature_files = models.FileField(upload_to=get_user_signature_path, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
