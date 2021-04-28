from django.shortcuts import render,redirect
from . models import Song,Podcast,Audiobook
# Create your views here.
from . forms import SongForm,PodcastForm,AudiobookForm

def home(request):
    return render(request,'index.html')

def song_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = SongForm()
        else:
            song = Song.objects.get(pk=id)
            form = SongForm(instance=song)
            return render(request,'song_form.html',{'form':form})
    else:
        if id == 0:
            form = SongForm(request.POST)

        else:
            song = Song.objects.get(pk=id)
            form = SongForm(request.POST,instance=song)

        if form.is_valid():
            print('Alekhya')
            form.save()
            return redirect('/songs_list/')

    return render(request, 'song_form.html', {'form': form})



def songs_list(request):
    songs = Song.objects.all()
    return render(request,'songs_list.html',{'songs':songs})

def song_delete(request,id):
    song = Song.objects.get(pk=id)
    song.delete()
    return redirect('/songs_list/')

def individual(request,id):
    songs = Song.objects.get(pk=id)
    return render(request,'individual_song.html',{'songs':songs})



# For podcasts
def podcast_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = PodcastForm()
        else:
            podcast = Podcast.objects.get(pk=id)
            form = PodcastForm(instance=podcast)
            return render(request,'podcast_form.html',{'form':form})
    else:
        if id == 0:
            form = PodcastForm(request.POST)
        else:
            podcast = Podcast.objects.get(pk=id)
            form = PodcastForm(request.POST,instance=podcast)

        if form.is_valid():
            form.save()
            return redirect('/podcasts_list/')
    return render(request, 'podcast_form.html', {'form': form})


def podcast_list(request):
    podcasts = Podcast.objects.all()
    print(podcasts)
    return render(request,'podcast_list.html',{'podcasts':podcasts})

def podcast_delete(request,id):
    podcast = Podcast.objects.get(pk=id)
    podcast.delete()
    return redirect('/podcasts_list/')

def individual_podcast(request,id):
    podcast = Podcast.objects.get(pk=id)
    return render(request,'individual_podcast.html',{'podcast':podcast})

# For audiobook

def audiobook_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = AudiobookForm()
        else:
            audiobook = Audiobook.objects.get(pk=id)
            form = AudiobookForm(instance=audiobook)
            return render(request,'audiobook_form.html',{'form':form})
    else:
        if id == 0:
            form = AudiobookForm(request.POST)
        else:
            audiobook = Audiobook.objects.get(pk=id)
            form = AudiobookForm(request.POST,instance=audiobook)

        if form.is_valid():
            form.save()
            return redirect('/audiobook_list/')
    return render(request, 'audiobook_form.html', {'form': form})


def audiobook_list(request):
    audiobooks = Audiobook.objects.all()
    return render(request,'audiobook_list.html',{'audiobooks':audiobooks})

def audiobook_delete(request,id):
    audiobook = Audiobook.objects.get(pk=id)
    audiobook.delete()
    return redirect('/audiobook_list/')

def individual_audiobook(request,id):
    audiobook = Audiobook.objects.get(pk=id)
    return render(request,'individual_audiobook.html',{'audiobook':audiobook})

