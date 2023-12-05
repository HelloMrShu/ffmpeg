
import os
from subprocess import check_call

filename = "./videos/2.flv"
output = "./output/2.mp4"
cmd = "ffmpeg -i {0} -vcodec copy -acodec copy {1}".format(filename, output)
if filename.endswith(".mp4"):
    data = os.system(cmd)
