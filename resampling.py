import wave
import os
import audioop

# resample audios from 44100 Hz refresh rate and 2 channels to 16000 Hz and 1 channels
# Audios were already 16 bits per sample


def resampleWav(src, inrate=44100, outrate=16000, inchannels=2, outchannels=1):
    dst = src[:-4] + "_resampled.wav"
    
    s_read = wave.open(src, 'r')
    s_write = wave.open(dst, 'w')

    n_frames = s_read.getnframes()
    data = s_read.readframes(n_frames)
    
    converted = audioop.ratecv(data, 2, inchannels, inrate, outrate, None)
    if outchannels == 1:
        converted = audioop.tomono(converted[0], 2, 1, 0)

    s_write.setparams((outchannels, 2, outrate, 0, 'NONE', 'Uncompressed'))
    s_write.writeframes(converted)

    s_read.close()
    s_write.close()


path = "Audios/ParishkarWorld_Q&A/0.wav"
file = wave.open(path)

for i in range(0,13):
    resampleWav(path[:-5]+str(i)+".wav")
    print(str(i)+" done")
    
for i in range(0,13):
    os.remove(path[:-5]+str(i)+".wav")
    
for i in range(0,13):
    os.rename(path[:-5]+str(i)+"_resampled.wav",path[:-5]+str(i)+".wav")
