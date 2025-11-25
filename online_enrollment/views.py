from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Course, Profile, Enrollment
from .forms import StudentForm, CourseForm, ProfileForm, UserForm, EnrollmentForm

@login_required
def home(request):
    return render(request, 'online_enrollment/home.html')

@login_required
def profile_view(request):
    # Ensure profile exists
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'online_enrollment/profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('online_enrollment:profile')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'online_enrollment/profile_edit.html', context)

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'online_enrollment/student_list.html', {'students': students})

@login_required
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('online_enrollment:students')
    else:
        form = StudentForm()
    return render(request, 'online_enrollment/student_form.html', {'form': form, 'title': 'Add Student'})

@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('online_enrollment:students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'online_enrollment/student_form.html', {'form': form, 'title': 'Edit Student'})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('online_enrollment:students')
    return render(request, 'online_enrollment/student_confirm_delete.html', {'student': student})

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'online_enrollment/course_list.html', {'courses': courses})

@login_required
def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('online_enrollment:courses')
    else:
        form = CourseForm()
    return render(request, 'online_enrollment/course_form.html', {'form': form, 'title': 'Add New Subject'})

@login_required
def course_edit(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('online_enrollment:courses')
    else:
        form = CourseForm(instance=course)

    return render(request, 'online_enrollment/course_edit.html', {'form': form})


@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('online_enrollment:courses')
    return render(request, 'online_enrollment/course_confirm_delete.html', {'course': course})

# ---------------- Enrollment ----------------

@login_required
def enrollment_list(request):
    enrollments = Enrollment.objects.select_related('student', 'course').all()
    return render(request, 'online_enrollment/enrollment_list.html', {'enrollments': enrollments})

@login_required
def enrollment_add(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('online_enrollment:enrollment_list')
    else:
        form = EnrollmentForm()
    
    courses = Course.objects.all()
    students = Student.objects.all()
    
    return render(request, 'online_enrollment/enrollment_form.html', {
        'form': form,
        'courses': courses,
        'students': students,
        'title': 'Add Enrollment'
    })


@login_required
def enrollment_edit(request, id):
    enrollment = get_object_or_404(Enrollment, pk=id)
    
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('online_enrollment:enrollment_list')
    else:
        form = EnrollmentForm(instance=enrollment)
    
    courses = Course.objects.all()
    students = Student.objects.all()
    
    return render(request, 'online_enrollment/enrollment_form.html', {
        'form': form,
        'enrollment': enrollment,
        'courses': courses,
        'students': students,
        'title': 'Edit Enrollment'
    })


@login_required
def enrollment_delete(request, id):
    enrollment = get_object_or_404(Enrollment, pk=id)
    
    if request.method == 'POST':
        enrollment.delete()
        return redirect('online_enrollment:enrollment_list')
    
    return render(request, 'online_enrollment/enrollment_delete.html', {'enrollment': enrollment})