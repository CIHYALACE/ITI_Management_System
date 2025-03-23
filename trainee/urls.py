from django.urls import path
from trainee.views import(
    Trainees,
    TraineesHome,
    # TraineesList,
    TraineesListView,
    # AddTrainee,
    AddTraineeView,
    AddForm,
    # UpdateTrainee,
    UpdateTraineeView,
    # DeleteTrainee,
    DeleteTraineeView,
    # TraineeDetails,
    TraineeDetailView,
    DeletedTrainees,
    RestoreTrainee,
    HardDelete)

urlpatterns = [
    path('trainees', Trainees , name="TraineesPage"),
    path('home', TraineesHome , name="TraineesHome"),
    path('TraineesList', TraineesListView.as_view() , name="TraineesList"),
    path('TraineesList/<int:pk>',  TraineeDetailView.as_view() , name="traineeProfile"),
    path('AddTrainee',  AddTraineeView.as_view() , name="AddTrainee"),
    path('AddTraineeViaForm', AddForm , name="AddTraineeViaForm"),
    path('DeletedTrainees', DeletedTrainees , name="DeletedTrainees"),
    path('HardDelete/<int:trainee_id>', HardDelete , name="HardDeleteTrainee"),
    path('UpdateTrainee/<int:pk>', UpdateTraineeView.as_view() , name="UpdateTrainee"),
    path('DeleteTrainee/<int:pk>',  DeleteTraineeView.as_view() , name="DeleteTrainee"),
    path('RestoreTrainee/<int:trainee_id>', RestoreTrainee , name="RestoreTrainee"),
]