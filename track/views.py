from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from track.models import Tracks
from track.forms import TrackForm

# Create your views here.

tracks = Tracks.objects.all()
def TracksHome(request):
    return render(request, 'track/home.html')

def TracksList(request):
    tracks = Tracks.objects.filter(track_status=True)
    context = {'tracks': tracks}
    return render(request, 'track/tracksList.html', context)

def DeleteTrack(request, track_id):
    Tracks.objects.filter(pk=track_id).update(track_status=False)
    return redirect('TracksList')

def HardDelete(request, track_id):
    Tracks.objects.filter(pk=track_id).delete()
    return redirect('DeletedTracks')

def DeletedTracks(request):
    tracks = Tracks.objects.filter(track_status=False)
    context = {'tracks': tracks}
    return render(request, 'track/deletedTracks.html', context)

def UpdateTrack(request, track_id):
    track = get_object_or_404(Tracks, pk=track_id)
    if request.method == "POST":
        form = TrackForm(request.POST, instance=track)
        if form.is_valid():
            form.save()  # Save the changes
            messages.success(request, "Track updated successfully!")
            return redirect('TracksList')
    else:
        form = TrackForm(instance=track)

    return render(request, 'track/editTrack.html', {'form': form})

def RestoreTrack(request, track_id):
    Tracks.objects.filter(pk=track_id).update(track_status=True)
    return redirect('DeletedTracks')

def AddTrack(request):
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            track = form.save(commit=False)
            track.save()
            return redirect('TracksList')
    else:
        form = TrackForm()
    return render(request, 'track/AddTrack.html', {'form': form})

def TrackDetails(request, track_id):
    track =get_object_or_404(Tracks, pk=track_id)
    return render(request , "track/trackDetails.html" , {"track": track})