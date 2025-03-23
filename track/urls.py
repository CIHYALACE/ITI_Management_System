from django.urls import path 
from track.views import (TracksHome,
                         TracksList,
                         AddTrack,
                         DeletedTracks,
                         DeleteTrack,
                         HardDelete,
                         RestoreTrack,
                         TrackDetails,
                         UpdateTrack)

urlpatterns = [
    path('home/', TracksHome , name='TracksHome'),
    path('list', TracksList , name='TracksList'),
    path('details/<int:track_id>', TrackDetails, name='TrackDetails'),
    path('delete/<int:track_id>', DeleteTrack , name='DeleteTrack'),
    path('hardDelete/<int:track_id>', HardDelete, name='HardDeleteTrack'),
    path('update/<int:track_id>', UpdateTrack, name='UpdateTrack'),
    path('restore/<int:track_id>', RestoreTrack , name='RestoreTrack'),
    path('deleted', DeletedTracks , name='DeletedTracks'),
    path('add', AddTrack , name='AddTrack'),
]