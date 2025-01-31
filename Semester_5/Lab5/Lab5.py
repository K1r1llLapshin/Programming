import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft # Преобразование Фурье
import seaborn as sns
import sklearn

audio_data = "./DataLab5.mp3"
audio, sample_rate = librosa.load(audio_data) # Загружаем аудио 

""" Анализ сигнала """

spectrum = fft(audio) # Вычисляет преобразвание Фурье
frequencies = np.fft.fftfreq(len(spectrum), 1 / sample_rate) # Получаем массив частот

X = librosa.stft(audio) # Вычисляем краткосрочное преобразование Фурье
Xdb = librosa.amplitude_to_db(abs(X)) # Преобразуем амплитуды спектра из линейной шкалы в децибелы


plt.figure('Анализ сигнала',figsize=(17, 9))

plt.subplot(2, 2, (1,2))
librosa.display.waveshow(audio, sr=sample_rate) # Отрисовываем сигнал в амплетудно-временной форме
plt.title('Амплетудно-временная форма')

plt.subplot(2, 2, 3)
plt.plot(frequencies[:len(frequencies)//2], np.abs(spectrum[:len(spectrum)//2])) # Берет только первую половину массивов frequencies и spectrum
plt.xlabel('Частота (Hz)')
plt.ylabel('Амплитуда')
plt.title('Частотный спектр')
plt.grid(True)

plt.subplot(2, 2, 4)
librosa.display.specshow(Xdb, sr=sample_rate, x_axis='time', y_axis='hz')
plt.colorbar()
plt.title('Спектрограмма')



""" Признаки """

y_harmonic, y_percussive = librosa.effects.hpss(audio) # Выделяем дорожку с битами
tempo, beat_frames = librosa.beat.beat_track(y=y_percussive,sr=sample_rate) # Определяем темп и бит фреймс
beat_times = librosa.frames_to_time(beat_frames, sr=sample_rate) # Преобразовываем
beat_time_diff=np.ediff1d(beat_times)# Вычисляем разность между битами
beat_nums = np.arange(1, np.size(beat_times)) # Создаём массив номеров битов 
print('Detected Tempo: '+str(tempo)+ ' beats/min')
print(beat_nums)

'''
fig, ax = plt.subplots()
fig.set_size_inches(15, 5)
ax.set_ylabel("Time difference (s)")
ax.set_xlabel("Beats")
g=sns.barplot(beat_time_diff,  palette="BuGn_d",ax=ax)
g=g.set(xticklabels=[])

sns.barplot принимает только одно значение, а передовалась в него два: beat_time_diff и beat_nums. Из-за чего была ошибка.
'''
# Нормализация спектрального центроида для визуализации
def normalize(y, axis=0):
    return sklearn.preprocessing.minmax_scale(y, axis=axis)

mfccs = librosa.feature.mfcc(y=y_harmonic, sr=sample_rate, n_mfcc=20) # Вычисляем мел-кепстральные коэффициенты 
cent = librosa.feature.spectral_centroid(y=audio, sr=sample_rate) # Вычисляем спектральный центроид

plt.figure('Признаки',figsize=(17, 9))

plt.subplot(2, 1, 1)
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCC')
print("MFCC (NumPy массив):\n", mfccs)

plt.subplot(2, 1, 2)
spectral_centroids = cent[0]
spectral_centroids.shape
frames = range(len(spectral_centroids))# Вычисление временной переменной для визуализации
t = librosa.frames_to_time(frames)
librosa.display.waveshow(audio, sr=sample_rate, alpha=0.4)# Отрисовываем сигнал в амплетудно-временной форме
plt.plot(t, normalize(spectral_centroids), color='b')# Отрисовываем спектральный центроид
plt.show()


'''
Вопрос: Что такое гармоническая и перкуссионная части сигнала и зачем они нужны?

Гармоническая часть сигнала характеризуется синусоидальной волной определенной частоты, 
которая обычно отвечает за высоту звука. В музыке это часто используется в струнных инструментах, 
таких как гитара или скрипка.

Перкуссионная часть сигнала, напротив, представляет собой острые импульсы, сосредоточенные во времени 
и проявляющиеся как резкие скачки. В музыке это типично для ударных инструментов, таких как барабаны.

В жизни все звуки представляют собой комбинацию гармонической и перкуссионной составляющих, и порой 
не всегда можно четко различить, где заканчивается одна и начинается другая.

'''