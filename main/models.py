from django.db import models
from django.utils import timezone


# Create your models here.

class MainAnnouncement(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.pub_date = timezone.now()
        self.save()


