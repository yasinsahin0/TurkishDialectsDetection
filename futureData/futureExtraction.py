import librosa
import pandas as pd
import numpy as np
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

class FutureExtraction:

    def __init__(self):
        pass

    def mfcc_extraction(self, sound_path, class_name):
        data, sample_rate = librosa.load(sound_path)

        mfcc = librosa.feature.mfcc(y=data, sr=sample_rate,n_mfcc=40)
        print(mfcc)
        np.savetxt("futureData/mfcc.txt",mfcc)
        # file = open("futureData/mfcc.txt","a")
        # file.write(class_name +","+str(mfcc))
        # file.close()



# FE = FutureExtraction()
# FE.mfcc_extraction("sound_split/sounds/1_tatarca_1.mp3","yeni")
# markers = np.fromfile('futureData/mfcc.txt')
# print(markers,sep=' ')