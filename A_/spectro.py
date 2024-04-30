import numpy
from scipy.io import wavfile
import PIL.Image as img
import PIL.ImageDraw as draw

IMAGE_SIZE = (350, 441)
FRAMERATE = 60.0
SECONDS_PER_RESET = 3.5
samples_per_chunk = (IMAGE_SIZE[0]*IMAGE_SIZE[1]) / (SECONDS_PER_RESET*FRAMERATE)

samplerate, data = wavfile.read('C:/Song2/A_/A_.wav')
wav_time = data.size/samplerate/2.0
total_frames = wav_time*FRAMERATE

running_img = img.new(mode="RGB", size=IMAGE_SIZE)
curr_pos = [0, 0]
curr_sample = 0


def clamp(n, smallest, largest): return max(smallest, min(n, largest))


def return_next_chunk(sample_pass: int, convert = True):
    out = []
    for sample in range(sample_pass, int(sample_pass+samples_per_chunk)):
        if not convert:
            out.append(data[sample][0])
        else:
            out.append(clamp(float(data[sample][0])/2147483392.0/2.0+0.5, 0.0, 1.0))

    return out


for frame in range(total_frames):
    chunk = return_next_chunk(curr_sample)
    curr_sample += samples_per_chunk

    # running_img.putpixel(xy=(curr_pos[0], curr_pos[1]), )

    if curr_pos[0] >= IMAGE_SIZE[0]-1 and curr_pos[1] >= IMAGE_SIZE[1]-1:
        running_img = img.new(mode="RGB", size=IMAGE_SIZE)
        curr_pos = [0, 0]



