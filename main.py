import wave
import numpy
import os, glob
import librosa


wav_files=[]
path=r"C:\Users\Marcin\Desktop\Projekty\SSI_cat_dog\archive\cats_dogs\train\cat\cat_1.wav"
# for file in glob.glob(path2):
#   print(file)

y, sr = librosa.load(path)
print(y)
# filenames = next(os.walk(path2))[2]
# print(filenames)


ifile= wave.open(path)
samples=ifile.getnframes()
audio=ifile.readframes(samples)

#converting with numpy
audio_int=numpy.frombuffer(audio, dtype=numpy.int16)
audio_float=audio_int.astype(numpy.float32)

#Normalization float to -1.0 : +1.0 range
maxint=2**15
audio_normalised=audio_float/maxint
print(audio_normalised)
