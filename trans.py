from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=kMCSMrnVsek")
title = video.title
print(title)

for key, value in video.__dict__.items():
    print(f"{key} = {value}")
