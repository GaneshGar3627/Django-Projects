from django.shortcuts import render
import requests
from django.conf import settings

from isodate import parse_duration


def classify(x):
    x = int(x)
    output = ''
    if (x < 9999):
        output = x
    elif (x >= 10000 and x < 1000000):
        x = x // 1000
        output = str(x) + 'K'
    elif (x >= 1000000 and x < 10000000):
        x = x // (1000 * 1000)
        output = str(x) + 'M'
    elif (x >= 10000000 and x < 1000000000):
        x = x // (10000000)
        output = str(x) + 'Cr'
    elif (x >= 1000000000 and x < 10000000000):
        x = x // (1000 * 1000 * 1000)
        output = str(x) + 'B'

    print(output)
    return output


def conscience(x):
    for i in x:
        print(i['views'])
        print(i['CommentCount'])
        print(i['likes'])
        print(i['dislikes'])
        i['SCORE'] = round(0.5*int(i['views'])+0.2*int(i['CommentCount'])+0.3*int(i['likes'])-0.1*int(i['dislikes']))

    Score = sorted(x, key=lambda i: int(i['SCORE']), reverse=True)
    return Score




def manager(VIDEOS):
    print("allow me to manage")
    duration = sorted(VIDEOS, key=lambda i: int(i['duration']))
    likes = sorted(VIDEOS, key=lambda i: int(i['likes']), reverse=True)
    dislikes = sorted(VIDEOS, key=lambda i: int(i['dislikes']))
    views = sorted(VIDEOS, key=lambda i: int(i['views']), reverse=True)
    comment = sorted(VIDEOS, key=lambda i: int(i['CommentCount']))
    date = sorted(VIDEOS, key=lambda i: i['Creation_date'], reverse=True)
    return likes, views, duration, date


def beautify(x):
    Beaut = []
    for i in x:
        video_data = {
            'title': i['title'],
            'id': i['id'],
            'thumbnail': i['thumbnail'],
            'url': i['url'],
            'duration': i['duration'],
            'likes': classify(i['likes']),
            'dislikes': classify(i['dislikes']),
            'views': classify(i['views']),
            'CommentCount': classify(i['CommentCount']),
            'Creation_date': i['Creation_date'][0:10],
            'channeltitle': i['channeltitle'],
        }
        Beaut.append(video_data)
    return Beaut


# Create your views here.
def first(request):
    VIDEOS = []
    w = []
    z = []
    x = []
    y = []
    rec=[]
    if request.method == 'POST':
        SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
        VIDEO_URL = "https://www.googleapis.com/youtube/v3/videos"
        print("\n\n\n sTARTS HERE \n\n\n\n")

        search_params = {
            'part': 'snippet',
            'q': request.POST['search'],
            'key': settings.YOUTUBE_DATA_API_KEY,
            'maxResults': 10,
            'type': 'video'
        }
        video_id = []

        r = requests.get(SEARCH_URL, params=search_params)

        #print("\n\nfirst", r.json()['items'][0])
        print("\n\nfirst", r.text)

        results = r.json()['items']

        for i in results:
            print(f"\n\n Vedio Id : {i['id']['videoId']}")
            video_id.append(i['id']['videoId'])

        # Video starts here

        video_params = {
            'key': settings.YOUTUBE_DATA_API_KEY,
            'part': 'snippet,statistics,contentDetails,id',
            'id': ','.join(video_id),
            'maxResults': 10,
        }

        vr = requests.get(VIDEO_URL, params=video_params)
        print("\n\n try understanding : \n\n\n", vr.text)
        v_result = vr.json()['items']

        """
        print("number of items :",len(v_result))
        print("items of response :")
        for i in v_result:
            print("members inside item : ")
            for j in i:
                print("child : ",j)
        print(v_result)
        print(" Zero\n\n\n\n",v_result[0]) """

        for i in v_result:
            print(i['kind'])
            try:
                video_data = {
                    'title': i['snippet']['title'],
                    'id': i['id'],
                    'thumbnail': i['snippet']['thumbnails']['high']['url'],
                    'url': f"https://www.youtube.com/watch?v={i['id']}",
                    'duration': int(parse_duration(i['contentDetails']['duration']).total_seconds() // 60),
                    'likes': (i['statistics']['likeCount']),
                    'dislikes': (i['statistics']['dislikeCount']),
                    'views': (i['statistics']['viewCount']),
                    'CommentCount': (i['statistics']['commentCount']),
                    'Creation_date': i['snippet']['publishedAt'],
                    'channeltitle': i['snippet']['channelTitle']
                }
                print(f"  gives data as :\n\n {video_data}")
                VIDEOS.append(video_data)
            except:
                print("ok proceed error has occured")

            print("looooooook atttt meeeee")
        rec = conscience(VIDEOS)
        w, x, y, z = manager(VIDEOS)
        w = beautify(w)
        x = beautify(x)
        y = beautify(y)
        z = beautify(z)
        print(f"x\n\ny\n\nz\n\n")
        print(f"{x}\n\n {y} \n\n  {z} \n\n")

    context = {
        'videos': VIDEOS,
        'Mliked': w,
        'Mviewd': x,
        'Mduration': y,
        'timeline': z,
        'recomend': rec,
    }

    return render(request, 'Vsearch/find.html', context)
