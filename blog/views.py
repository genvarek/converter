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