from django.shortcuts import render
from django.http import HttpResponse
from .forms import Ddownload
import os

global video_url

from pytube import YouTube


# Create your views here.


def greetings(request):
    return render(request, 'Download/test2.html')


def download(request):
    if request.method == 'POST':
        video_url = request.POST['video_url']
        # video_url = 'https://www.youtube.com/watch?v=LIlmQ8xhRRI'
        yt = YouTube(video_url)
        STREAM_LIST = yt.streams
        res = render(request, 'Download/test2.html', {'STREAM_LIST': STREAM_LIST, "video_url": video_url})
        return res
    else:
        res = render(request, '')
        return res


# start main method

def goddownloads(link, tag):
    #os.chdir('C:/Users/shivv/Downloads/pytube_downloads')
    yt = YouTube(link)
    god = yt.streams.get_by_itag(tag).download()
    pre = os.path.split(god)[0]
    suf = os.path.split(god)[1]
    suf = ''.join(suf.split())
    print(f"{pre} , {suf}")
    goddessess = os.path.join(pre, suf)

    print(f"god is : {god}")

    print(f"goddessess is : {goddessess}")

    try:
        os.rename(god, goddessess)
    except:
        print("An exception occurred")




    FILE_NAME = os.path.split(os.path.splitext(goddessess)[0])[1]
    print(FILE_NAME)
    return FILE_NAME


def godSearches(imp):
    for dirpath, dirnames, filenames in os.walk('C:/Users/shivv/PycharmProjects/Django/YouTU/media/Downloaded/Single'):
        for i in filenames:
            main_path = os.path.splitext(os.path.join(dirpath + "/", i))
            if os.path.split(main_path[0])[1] == imp:
                print("Name :", i)
                print("Base Name :", os.path.basename(i))
                print("Directory :", os.path.dirname(dirpath))
                print("Split :", os.path.split(dirpath))
                raasta = os.path.join(dirpath + "/", i)
                print("Actual path :", os.path.join(dirpath + "/", i))
                print("Split directory path :", os.path.splitext(os.path.join(dirpath + "/", i)))
                main_path = os.path.splitext(os.path.join(dirpath + "/", i))
                print("File Name:", os.path.split(main_path[0])[1])
                print("look here man",os.getcwd())
                print('\n')

    return raasta


def sweet(request):
    if request.method == 'POST':
        video_url_redirect = request.POST['video_url_d']
        itag = request.POST['ITAG']
        print(os.getcwd())
        os.chdir('C:/Users/shivv/PycharmProjects/Django/YouTU/media/Downloaded/Single')
        print(os.getcwd())
        safe=goddownloads(video_url_redirect, itag)

        loc = godSearches(safe)
        print(loc)
        SIZE = (os.stat(loc).st_size)/(1024*1024)
        loc = loc.replace('C:/Users/shivv/PycharmProjects/Django/YouTU', '')


        print(video_url_redirect)
        print(itag)

    return render(request, 'Download/test3.html', {"location":loc,'SIZE':SIZE,'Name':safe})


def downloading(request):
    if request.method == 'POST':
        formatRadio = request.POST['formatRadio']
        if formatRadio != "audio":
            qualityRadio = request.POST['qualityRadio']
        video_url_d = request.POST['video_url_d']
        print(formatRadio)
        # print(qualityRadio)
        yt = YouTube(video_url_d)
        print(yt)
        print("Downloading start ....")
        if formatRadio == "audio":
            yt.streams.filter(type=formatRadio).last().download()
        else:
            yt.streams.filter(type=formatRadio, resolution=qualityRadio).first().download()
        print("Downloding completed")
    res = render(request, 'Download/test2.html', {"msg": "downloading completed"})
    return res


"""
def yt_download(request):
    if request.method == 'POST':
        form = Ddownload(request.POST)
        #title = form.cleaned_data['title']
        if form.is_valid():
            print(form.errors)
            print("error here")
            title = form.POST['title']
            print(title)
            yt = YouTube(title)
            rresolution = []
            strm_all = yt.streams.all()

            for i in strm_all:
                rresolution.append(i.resolution)

            rresolution = list(dict.fromkeys(rresolution))
            print(rresolution)
            matter = {
                'res': rresolution,
                'links': title,
            }
    context = {
        'material': matter
    }


    form = Ddownload()
    return render(request, 'Download/test1.html', context)
"""

"""
def yt_download(request):
    link = request.POST['search']

    if request.method == 'POST':
        yt = YouTube(link)
        rresolution = []
        strm_all = yt.streams.all()

        for i in strm_all:
            rresolution.append(i.resolution)

        rresolution = list(dict.fromkeys(rresolution))
        print(rresolution)
        embed_link = link.replace("watch?v=", "embed/")

        matter = {
            'res': rresolution,
            'links': link,
            'embed': embed_link
        }

    context = {
        'material': matter
    }

    return render(request, 'Download/yt_download.html', context)
"""

"""
def download2(request):
    url = request.GET.get('url')
    print(f'url  :{url}')
    yt = YouTube(url)
    rresolution = []

    strm_all = yt.streams.all()

    for i in strm_all:
        rresolution.append(i.resolution)

    rresolution = list(dict.fromkeys(rresolution))

    print(f'resolutions : {rresolution}')
    embed_link = link.replace("watch?v=", "embed/")

    return render(request, 'Download/yt_D2.html', {'title': 'D2', 'Resolutions': rresolution, 'embed': embed_link})
"""
