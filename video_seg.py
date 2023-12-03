# ffmpeg -i video.mp4 -vf "select=eq(n\,0)" -vframes 1 first_frame.jpg

import os
from subprocess import check_call

filename = "./videos/1.mp4"
start = "00:00:00"
end = "00:00:10"
length = 10
output1 = "./output/segment_1.mp4"
output2 = "./output/segment_2.mp4"
cmd1 = "ffmpeg -i {0} -c:v libx264 -crf 18 -ss {1} -to {2} {3}".format(filename, start, end, output1)
cmd2 = "ffmpeg -i {0} -c:v libx264 -crf 18 -ss {1} -t {2} {3}".format(filename, start, length, output2)
if filename.endswith(".mp4"):
    data1 = os.system(cmd1)
    data2 = os.system(cmd2)
    print(data1, data2)
