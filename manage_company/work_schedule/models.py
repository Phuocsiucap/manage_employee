from django.db import models

# Create your models here.
class work_schedule(models.Model):
    
    MORNING = 'Morning'
    AFTERNOON = 'Afternoon'
    FULL_DAY = 'Full_day'
    
    SHIFT_CHOICES = [
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (FULL_DAY, 'Full day'),
    ]
    
    
    id = models.AutoField(primary_key=True)
    employee_id = models.IntegerField()
    work_day = models.DateField()
    shift = models.CharField(max_length=30, choices=SHIFT_CHOICES)  # e.g., 'Morning', 'Afternoon', 'Night'
    
    
    def save(self, *args, **kwargs):
        # Custom save logic can be added here
        super(work_schedule, self).save(*args, **kwargs)