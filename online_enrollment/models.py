from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# ---------------- Profile ----------------
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

# Automatically create and save Profile for each new User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()


# ---------------- Student ----------------
class Student(models.Model):
    stud_id = models.IntegerField(null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField('Course', blank=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)  # Use CharField

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ---------------- Course ----------------
class Course(models.Model):
    code = models.CharField(max_length=100)  # new field
    description = models.TextField(blank=True)
    instructor = models.CharField(max_length=100, blank=True)
    room = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=50, blank=True)
    time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.code

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.course}"


