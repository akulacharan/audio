from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    # for song
    path('song_form/',views.song_form,name='song_form'),
    path('songs_list/',views.songs_list,name='songs_list'),
    path('<int:id>/',views.song_form,name='update_song'),
    path('delete/<int:id>/',views.song_delete,name='delete_song'),
    path('individual_song/<int:id>/',views.individual,name='individual_song'),

    # for podcast
    path('podcast_form/',views.podcast_form,name='podcast_form'),
    path('podcasts_list/',views.podcast_list,name='podcasts_list'),
    path('podcast/<int:id>/',views.podcast_form,name='update_podcast'),
    path('poddelete/<int:id>/',views.podcast_delete,name='delete_podcast'),
    path('individual_podcast/<int:id>/',views.individual_podcast,name='individual_podcast'),

    #for audiobook

    path('audiobook_form/',views.audiobook_form,name='audiobook_form'),
    path('audiobook_list/',views.audiobook_list,name='audiobook_list'),
    path('audiobook/<int:id>/',views.audiobook_form,name='update_audiobook'),
    path('audiodelete/<int:id>/',views.audiobook_delete,name='delete_audiobook'),
    path('individual_audiobook/<int:id>/', views.individual_audiobook, name='individual_audiobook'),

]