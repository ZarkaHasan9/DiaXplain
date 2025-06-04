from django.db import models
from django.contrib.auth.models import User
# Create your models here. 
class Prediction(models.Model):
    # define fields, for example:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_data = models.TextField()
    result = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Report(models.Model):
    prediction = models.ForeignKey(Prediction, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)
    generated_at = models.DateTimeField(auto_now_add=True)
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name}"

