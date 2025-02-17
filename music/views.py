from django.shortcuts import render, redirect,get_object_or_404
from .models import Music


def music_list(request):
    music = Music.objects.all()
    ctx = {'music':music}
    return render(request, 'music/music-list.html', ctx)

def create_album(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        artist=request.POST.get('artist')
        date=request.POST.get('date')
        genre=request.POST.get('genre')
        if title and artist and date and genre:
            Music.objects.create(
                title = title,
                artist = artist,
                date = date,
                genre = genre
            )
            return redirect('music:list')
    return render(request, 'music/album-create.html')

def album_detail(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    ctx = {'music':music}
    return render(request, 'music/album-detail.html', ctx)

def album_update(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    if request.method == 'POST':
        title=request.POST.get('title')
        artist=request.POST.get('artist')
        date=request.POST.get('date')
        genre=request.POST.get('genre')
        if title and artist and date and genre:
            music.title = title
            music.artist = artist
            music.date = date
            music.genre = genre
            music.save()
            return redirect(music.get_detail_url())
    ctx = {'music':music}
    return render(request, 'music/album-create.html', ctx)

def album_delete(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    music.delete()
    return redirect('music:list')