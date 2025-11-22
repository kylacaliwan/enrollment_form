from django import forms
from django.contrib.auth.models import User
from .models import Student, Course, Profile, Enrollment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['contact_number', 'address']  # Only fields that exist on Profile
        widgets = {
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['stud_id', 'first_name', 'last_name', 'email', 'contact_number']
        widgets = {
            'stud_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student ID'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'description', 'instructor', 'room', 'department', 'time']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject Code'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'instructor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Instructor'}),
            'room': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Room'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM'}),
        }


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']  # Include both
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
        }