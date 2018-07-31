from django.views import generic
from .models import Album, Song
from .forms import CreateAlbum
from django.shortcuts import render


class IndexView(generic.ListView):
    template_name = 'templates/index.html'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Song
    template_name = 'templates/detail.html'


def Albumform(request):
    form = CreateAlbum()
    if request.method == 'POST':
        form = CreateAlbum(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return IndexView(request)
    return render(render, 'templates/album_form.html', {'form': form})
