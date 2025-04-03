from django.db import models
# Create your models here.
class Yolo(models.Model):
    ## id(p.k), name, aiexplain,
    # original_img, result_img, today
    objects = None
    name = models.CharField(max_length=20)
    aiexplain = models.TextField()
    original_img = models.FileField(upload_to='yolo/original/')
    result_img = models.FileField(upload_to='yolo/result/')
    today = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}_{self.today}"
