from django.urls import path
from course.views import ( 
    CourseHome,
    CourseList,
    DeleteCourse,
    HardDelete,
    UpdateCourse,
    AddCourse,
    Login,
    Logout,
    Register,
    CourseDetails,
    DeletedCourses,
    RestoreCourse)

urlpatterns = [
    path('home', CourseHome , name='courseHome'),
    path('list', CourseList , name='courseList'),
    path('details/<int:id>', CourseDetails , name='courseDetails'),
    path('add', AddCourse , name='addCourse'),
    path('update/<int:course_id>', UpdateCourse , name='updateCourse'),
    path('delete<int:course_id>', DeleteCourse , name='deleteCourse'),
    path('hardDelete<int:course_id>', HardDelete , name='HardDeleteCourse'),
    path('deletedCourses', DeletedCourses , name='deletedCourses'),
    path('restore<int:course_id>', RestoreCourse , name='restoreCourse'),
    path('login', Login , name='login'),
    path('logout', Logout , name='logout'),
    path('register', Register , name='register'),
]