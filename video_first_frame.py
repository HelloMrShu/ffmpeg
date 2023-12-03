# ffmpeg -i video.mp4 -vf "select=eq(n\,0)" -vframes 1 first_frame.jpg

import os
from subprocess import check_call

filename = "./videos/1.mp4"
output = "./output/first_frame.jpg"
cmd = "ffmpeg -i {0} -vf 'select=eq(n\,0)' -vframes 1 {1}".format(filename, output)
if filename.endswith(".mp4"):
    data = os.system(cmd)
    # check_call(cmd)
