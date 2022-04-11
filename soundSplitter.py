import os
import librosa

class SoundSplitter:

    def __init__(self):
        self.root_path = os.getcwd() + "/"
        self.sound_path = self.root_path + "sound_download"
        self.sound_split_file = self.root_path + "sound_split"

    def SoundFileNameList(self):
        file_list = os.listdir(self.sound_path)
        for name in file_list:
            if name.find(".") >= 0:
                file_list.remove(name)
        return file_list

    

nesne = SoundSplitter()
nesne.SoundFileNameList()