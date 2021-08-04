import sys
import os
import sys
import time
import socket

try:
    import youtube_dl
except Exception as e:
    os.system('pip install youtube_dl')
    import youtube_dl

def play(song):
    hostname = socket. gethostname()
    IPAddr = socket. gethostbyname(hostname)
    ydl_opts = {}
    if not os.path.isdir('music/'):
        os.mkdir('music/')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info('ytsearch:'+song, download=False)
        video_title = info_dict.get('title', None)

    ydl_opts = {
        'postprocessor_args': ['-loglevel', 'panic'],
        'source_address': f'{IPAddr}',
        'outtmpl': f'music/{song}.mp3',
        'default-search':'ytsearch',
        'format': 'bestaudio/best'
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['ytsearch:{}'+song])
    os.system('cls')
    print("successfully downloaded: ",song)
while True:
    os.system('color a')
    play(input("name of the song u wanna download: "))
