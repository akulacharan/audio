from django import forms

from .models import Song,Podcast,Audiobook

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('name','duration',)
        labels = {
            'name': 'Name',
            'duration': 'Duration',

        }


class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = ('name','duration','host','participants')


class AudiobookForm(forms.ModelForm):
    class Meta:
        model = Audiobook
        fields = ('title','author','narrator','duration')