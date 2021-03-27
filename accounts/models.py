from django.db import models

# Create your models here.
class Courses(models.Model):
    course_id = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    def __str__(self):
        return self.course_id

class Saved_Data(models.Model):
    course_id = models.CharField(max_length=10)
    position = models.IntegerField()
    #label divs as '1, 2, 3, 4'... so 1 is a course saved in
    #the available courses div, and 2 is the first semester, and so on

class Semesters(models.Model):
    semester_id = models.CharField(max_length=10)
    title = models.CharField(max_length=10)

class Offered_In(models.Model):
    semester_id = models.CharField(max_length=10)
    CS1000 = models.IntegerField()
    CS1010 = models.IntegerField()
