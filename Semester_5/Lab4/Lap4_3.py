import cv2
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('-dir')
parser.add_argument('-save')

args = parser.parse_args() 

video = cv2.VideoCapture(args.dir)  

ret, frame = video.read()
fps = video.get(cv2.CAP_PROP_FPS) # Получаем FPS
w = video.get(cv2.CAP_PROP_FRAME_WIDTH) # Получаем ширину
h = video.get(cv2.CAP_PROP_FRAME_HEIGHT) # Получаем высоту 
name = Path(args.dir).name  # Получаем имя файла

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Кодек для сохранения видео
out = cv2.VideoWriter(args.save, fourcc, fps, (int(w), int(h)))  # Создаем объект VideoWriter

while True:
    ret, frame = video.read()
    if not ret:
        break

    cv2.putText(frame, f"NAME: {name}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)
    cv2.putText(frame, f"FPS: {fps // 1}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)
    cv2.putText(frame, f"WIDTH: {w} px", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)
    cv2.putText(frame, f"HEIGHT: {h} px", (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)
    cv2.imshow('Lab4', frame) # выводим на экран
    out.write(frame)  # Записываем кадр в видеофайл
    
    if cv2.waitKey(25) & 0xFF == ord('q'): # Остовить просмотр досрочно, нажав q
        break

video.release()
out.release()
cv2.destroyAllWindows()