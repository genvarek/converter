"""from django.shortcuts import render, redirect

def post_list(request):
    return render(request, 'blog/templates/blog/post_list.html', {})

import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

with ydl:
    result = ydl.extract_info(
        'http://www.youtube.com/watch?v=BaW_jenozKc',
        download=False  # We just want to extract the info
    )

if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result

print(video)
video_url = video['url']
print(video_url)"""

from django.shortcuts import render, redirect
from blog.models import Query
from blog.forms import QueryForm
import youtube_dl


def download_video(request):

    form = LinkForm()
    context = {
        'form': form
    }
    return render(request, 'post_list.html', context)

def post_list(request):
    links = Query.objects.all()

    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid:
            link = request.POST['link']
            with youtube_dl.YoutubeDL({'format': '134'}) as ydl:
                result = ydl.extract_info(link, download=False)
                video_url = result['url']
            form.save()
            return redirect(video_url)
    else:
        form = QueryForm()

    return render(request, 'post_list.html', {'links': links, 'form': form})






