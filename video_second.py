import os
from subprocess import check_call

file1 = "./videos/1.mp4"
moment = '00:10:00'
output = "./output/snap.png"
size = "352x240"

cmd = "ffmpeg -ss {0} -i {1} -y -f image2 -vframes 1 {2}".format(moment, file1, output)
cmd1 = "ffmpeg -ss 10 -i {0} -y -f image2  -vframes 1 -s {1} {2}".format(file1, size, output)
cmd2 = "ffmpeg -ss 3 -i {0} -y -f mjpeg -t 1 {1}".format(file1, output)

if file1.endswith(".mp4") or file1.endswith(".flv"):
    data = os.system(cmd1)
