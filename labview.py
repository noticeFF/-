import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz
from scipy.io.wavfile import write
import time

lowcut=300.0    #нижняя граница пропускания
highcut=3000.0  #верхняя граница пропускания
fs=44100    #частота дискретизации
order=4
duration=5.0
def butterwort(lowcut,highcut,fs,order=5):
    nyq=0.5*fs  # частота Найквиста
    low=lowcut/nyq
    high=highcut/nyq
    b,a=butter(order, [low, high], btype='band')
    return b, a

def filter(data,lowcut,highcut,fs,order=5):
    b, a=butterwort(lowcut,highcut,fs,order=order)
    y=lfilter(b, a, data)
    return y

def spectr(signal, title, fs):
    n = len(signal)
    freq = np.fft.rfftfreq(n,d=1/fs)
    fftSpectr = np.abs(np.fft.rfft(signal))
    plt.figure(figsize=(10,4))
    plt.plot(freq,fftSpectr)
    plt.title(f"спектр: {title}")
    plt.xlabel('частота')
    plt.ylabel('амплитуда')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    print("Запись звука началась...")
    audio=sd.rec(int(duration * fs),samplerate=fs,channels=1,dtype='float64')
    sd.wait()
    audio=audio.flatten()
    print("Запись звука завершилась")
    write("input.wav", fs, np.int16(audio * 32767))
    filtered=filter(audio,lowcut,highcut,fs, order)
    write("output.wav",fs,np.int16(filtered * 32767))
    spectr(audio, "начальый сигнал",fs)
    spectr(filtered, "конечный сигнал",fs)



main()
