from django.http import JsonResponse
from course.models import Courses
from course.serializer import CourseSerializer
from track.serializer import TrackSerializer
from trainee.serializer import TraineeSerializer
from trainee.models import TraineeProfile
from track.models import Tracks

# Create your views here.

def DjangoAPI(request):
    courses = Courses.objects.all()
    trainees = TraineeProfile.objects.all()
    tracks = Tracks.objects.all()

    course_serializer = CourseSerializer(courses, many=True)
    trainee_serializer = TraineeSerializer(trainees, many=True)
    track_serializer = TrackSerializer(tracks, many=True)

    data = {
        'courses': course_serializer.data,
        'trainees': trainee_serializer.data,
        'tracks': track_serializer.data
    }

    return JsonResponse(data, safe=False)