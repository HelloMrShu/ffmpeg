# ffmpeg -i video.mp4 -vf "select=eq(n\,0)" -vframes 1 first_frame.jpg

import os
from subprocess import check_call

filename = "./videos/1.mp4"
start = "00:00:00"
end = "00:00:10"
output = "./output/segment.mp4"
cmd = "ffmpeg -i {0} -c:v libx264 -crf 18 -ss {1} -to {2} {3}".format(filename, start, end, output)
if filename.endswith(".mp4"):
    data = os.system(cmd)
    print(data)
