from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import TraineeProfile
from trainee.forms import TraineeForm
from django.db.models import Case, When, Value, CharField, F
from django.views.generic import ListView, DetailView,UpdateView, CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
trainees = TraineeProfile.getalltrainee()

def Trainees(requist):
    return JsonResponse(list(TraineeProfile.objects.values()), safe=False)

def TraineesHome(requist):
    return render(requist , "trainee/home.html")

# Generic View
class TraineesListView(ListView):
    model = TraineeProfile
    template_name = "trainee/traineesList.html"
    context_object_name = 'trainees'

    def get_queryset(self):
        return TraineeProfile.objects.select_related('trainee_track').annotate(
            track_display=Case(
                When(trainee_track__track_status=True, then=F('trainee_track__track_name')),
                default=Value(None),
                output_field=CharField()
            )
        ).filter(trainee_status=True)

class TraineeDetailView(DetailView):
    model = TraineeProfile
    template_name = "trainee/traineeProfile.html"
    context_object_name = 'trainee'

class DeleteTraineeView(UpdateView):
    model = TraineeProfile
    fields = []
    template_name = "trainee/confirm_delete.html"
    success_url = reverse_lazy('TraineesList')

    def form_valid(self, form):
        self.object.trainee_status = False
        self.object.save()
        return super().form_valid(form)

# class-based view
class AddTraineeView(CreateView):
    model = TraineeProfile
    form_class = TraineeForm
    template_name = "trainee/addTrainee.html"
    success_url = reverse_lazy('TraineesList')

class UpdateTraineeView(UpdateView):
    model = TraineeProfile
    form_class = TraineeForm
    template_name = "trainee/updateTrainee.html"
    success_url = reverse_lazy('TraineesList')

    def get_object(self, queryset=None):
        """ Hook to ensure object is fetched based on the primary key from the URL """
        pk = self.kwargs.get('pk')
        return get_object_or_404(TraineeProfile, pk=pk)

# Function Based View
def RestoreTrainee(request, trainee_id):
    TraineeProfile.objects.filter(pk=trainee_id).update(trainee_status=True)
    return redirect('TraineesList')

def AddForm(requist):
    form = TraineeForm()
    return render(requist , "trainee/forms/addForm.html", context={'form': form})

def DeletedTrainees(requist):
    trainees = TraineeProfile.objects.filter(trainee_status=False)
    context={'trainees':trainees}
    return render(requist , "trainee/deletedTrainees.html" , context)

def HardDelete(requist, trainee_id):
    TraineeProfile.objects.filter(pk=trainee_id).delete()
    return redirect('DeletedTrainees')


# def TraineesList(requist):
#     trainees = TraineeProfile.objects.select_related('trainee_track').annotate(
#     track_display=Case(
#         When(trainee_track__track_status=True, then=F('trainee_track__track_name')),
#         default=Value(None),
#         output_field=CharField()
#     )
# ).filter(trainee_status=True)
#     return render(requist , "trainee/traineesList.html" , {'trainees':trainees})

# def TraineeDetails(requist, trainee_id):
#     trainee =get_object_or_404(TraineeProfile, pk=trainee_id)
#     return render(requist , "trainee/traineeProfile.html" , {"trainee": trainee})

# def AddTrainee(requist):
#     if requist.method == "POST":
#         data = requist.POST
#         TraineeProfile.objects.create(
#             trainee_first_name=data["firstName"],
#             trainee_last_name=data["lastName"],
#             trainee_email=data["email"],
#             trainee_phone=data["phone"],
#             trainee_address=data["address"]
#             )
#         return redirect('TraineesList')
#     else: 
#         return render(requist , "trainee/addTrainee.html")

# def UpdateTrainee(requist , trainee_id):
#     trainee = get_object_or_404(TraineeProfile, pk=trainee_id)
#     if requist.method == "POST":
#         data = requist.POST
#         trainee.trainee_first_name = data["firstName"]
#         trainee.trainee_last_name = data["lastName"]
#         trainee.trainee_email = data["email"]
#         trainee.trainee_phone = data["phone"]
#         trainee.trainee_address = data["address"]
#         trainee.save()
#         return redirect('TraineesList')
#     else:
#         return render(requist, "trainee/updateTrainee.html", {"trainee": trainee})

# def DeleteTrainee(request, trainee_id):
#     TraineeProfile.objects.filter(pk=trainee_id).update(trainee_status=False)
#     return redirect('TraineesList')