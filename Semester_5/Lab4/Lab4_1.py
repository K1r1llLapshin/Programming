from moviepy.editor import * 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-dir')
parser.add_argument('-start')
parser.add_argument('-end')
parser.add_argument('-save')

pars = parser.parse_args()

with VideoFileClip(pars.dir) as video:
    clip = video.subclip(pars.start, pars.end) # вырезаем клип из видео 
    comb = concatenate_videoclips([clip]) # соединяем его один для сохранения
    comb.write_videofile(pars.save) # сохраняем 

    
