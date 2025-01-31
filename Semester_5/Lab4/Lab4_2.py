from moviepy.editor import *
import argparse
import numpy as np
from skimage import transform, io
parser = argparse.ArgumentParser()
parser.add_argument('-dir')
parser.add_argument('-start', type=int)
parser.add_argument('-end', type=int)
parser.add_argument('-save')
parser.add_argument('-step', type=int, default=10)

pars = parser.parse_args()

with VideoFileClip(pars.dir) as video:
    count_frame = 1
    for frame_time in np.arange(pars.start, pars.end + pars.step, pars.step):
        frame = video.get_frame(frame_time) # берем кадр
        resize_frame = transform.resize(frame, (250, int(frame.shape[0] * 250 / frame.shape[1]))) # меняем его размер с сохраниением пропорций 
        resize_frame = (resize_frame * 255).astype(np.uint8) # Преобразуем изображение в формат uint8
        io.imsave(f"{pars.save}\\{count_frame}.png", resize_frame) # сохроняем кадр 
        count_frame += 1
        
    