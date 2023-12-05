import os

filename = "./videos/1.mp4"
output = "./output/%04d.jpg"
rate = 1/9
cmd = "ffmpeg -i {0} -vf fps={1} {2}".format(filename, rate, output)
if filename.endswith(".mp4"):
    data = os.system(cmd)
