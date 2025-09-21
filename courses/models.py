from django.db import models
from users.models import PersonDetails

# Create your models here.
class CourseDetails(models.Model):
    course_title = models.CharField(max_length = 100, null = False)
    course_authour = models.ForeignKey(
        PersonDetails,
        on_delete=models.CASCADE,
        limit_choices_to={'designation': 'Teacher'},  
        related_name='courses'
        )
    course_description = models.TextField(null = False)
    course_price = models.FloatField(null = False)
    course_thumbnail = models.ImageField(upload_to = 'courses/thumbnails', blank=True,null = True)
    course_duration = models.IntegerField(null = False) # duration in hours
    course_created_at = models.DateTimeField(auto_now_add = True)
    course_updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.course_title + ' by ' +self.course_authour.username
