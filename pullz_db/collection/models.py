from django.db import models

# Create your models here.
class Comic(models.Model):
    STATUS_CHOICES = [
        ('owned', 'Owned'),
        ('wanted', 'Wanted'),
    ]



    title = models.CharField(max_length=200)
    issue_number = models.IntegerField()
    release_date = models.DateField()
    coverType = models.CharField(max_length=50)
    condition = models.CharField(max_length=50, blank=True)

    writer = models.CharField(max_length=100, blank=True)
    artist = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=100, blank=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='owned')
    created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return f"{self.title} #{self.issue_number}"
