import os
import wave

waveFolder= ""
wavelist = []

# get a list of .wav files
for i in os.listdir(waveFolder):
    if i.find(".wav")>=0:
        wavelist.append(waveFolder+"/"+i)
    elif i.find(".WAV")>=0:
        wavelist.append(waveFolder+"/"+i)

if not wavelist :
    print("Warning NO '.wav' files")
else:
    print("{0:<45}".format('File Path'), 'Frame Rate  Width Chans Frames')
    for filename in wavelist:
        f = wave.open(filename,'rb')
        # the format string "{0:<50}" says print left justified from chars 0 to 50 in a fixed with string
        print("{0:<50}".format(filename),
              "{0:>5}".format(f.getframerate()),
              "{0:>5}".format(f.getsampwidth()),
              "{0:>6}".format(f.getnchannels()),
              "{0:>6}".format(f.getnframes())
              )
