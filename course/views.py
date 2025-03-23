from django.shortcuts import render , redirect , get_object_or_404
from .models import Courses
from django.db.models import Case, When, Value, CharField, F


# Create your views here.

def AddCourse(request):
    if request.method == "POST":
        data = request.POST
        Courses.objects.create(
            course_name=data["courseName"],
            course_duration=data["courseDuration"],
            course_fee=data["courseFee"],
            course_trainer=data["courseTrainer"],
            course_start_date=data["courseStartDate"],
            course_end_date=data["courseEndDate"]
        )
        return redirect('courseList')
    else:
        return render(request, 'course/addCourse.html')

def CourseHome(request):
    return render(request, 'course/home.html')

def CourseList(request):
    courses = Courses.objects.select_related('course_track').annotate(
    track_display=Case(
        When(course_track__track_status=True, then=F('course_track__track_name')),
        default=Value(None),
        output_field=CharField()
    )
).filter(course_status=True) 
    return render(request, 'course/courseList.html', {'courses': courses})

def CourseDetails(request,id):
    course = Courses.objects.get(course_id=id)
    return render(request, 'course/courseDetails.html', context={"course": course})

def DeleteCourse(request , course_id):
    Courses.objects.filter(pk=course_id).update(course_status=False)
    return redirect ('courseList')

def HardDelete(request , course_id):
    Courses.objects.filter(pk=course_id).delete()
    return redirect ('deletedCourses')

def RestoreCourse(request , course_id):
    Courses.objects.filter(pk=course_id).update(course_status=True)
    return redirect ('deletedCourses')

def UpdateCourse(request, course_id):
    coursee = get_object_or_404(Courses, pk=course_id)
    if request.method == "POST":
        data = request.POST
        coursee.course_name = data["course_name"]
        coursee.course_duration = data["course_duration"]
        coursee.course_fee = data["course_fee"]
        coursee.course_trainer = data["course_trainer"]
        coursee.course_start_date = data["course_start_date"]
        coursee.course_end_date = data["course_end_date"]
        coursee.save()
        return redirect('courseList')
    else:
        return render(request, 'course/updateCourse.html', {"course": coursee})

def DeletedCourses(request):
    courses = Courses.objects.filter(course_status=False)
    context = {'courses': courses}
    return render(request, 'course/deletedCourses.html', context)

def Login(request):
    return render(request, 'course/login.html')

def Logout(request):
    return render(request, 'course/logout.html')

def Register(request):
    return render(request, 'course/register.html')
