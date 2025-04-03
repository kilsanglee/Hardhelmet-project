from django.db import models

# Create your models here.

class Gemini2(models.Model):
    ##  id(p.k) , name, explain, aiexplain, filename, today
    objects = None
    name = models.CharField(max_length=20)
    explain = models.TextField()
    aiexplain = models.TextField()
    filename = models.CharField(max_length=35)
    file = models.FileField(upload_to='gemini/')
    today = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  f"{self.name}_{self.filename}"

class ChatGPT(models.Model):
    ##  id(p.k) , name, explain, aiexplain, filename, today
    objects = None
    name = models.CharField(max_length=20)
    explain = models.TextField()
    aiexplain = models.TextField()
    file = models.FileField(upload_to='chatgpt/')
    today = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}_{self.filename}"