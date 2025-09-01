from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique = True)
    position = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    start_date = models.DateField()
    
    def save(self, *args, **kwargs):
        # Custom save logic can be added here
        super(Employee, self).save(*args, **kwargs)