import os
import librosa

class SoundSplitter:

    def __init__(self):
        self.sound_file_path = 'sound_download/'
        self.splitter_path = 'sound_split/sounds/'
        self.data_create_path = "sound_split/data.csv"
        self.main_path = os.getcwd() +"/"

    def sound_data_list_create(self):
        sound_list = []
        sound_file_list = os.listdir(self.main_path+self.sound_file_path)
        for file_name in sound_file_list:
            if file_name.find(".") > 0:
                sound_file_list.remove(file_name)
        print(sound_file_list)
        self.root_path = os.getcwd() + "/"
        self.sound_path = self.root_path + "sound_download"
        self.sound_split_file = self.root_path + "sound_split"

    def SoundFileNameList(self):
        file_list = os.listdir(self.sound_path)
        for name in file_list:
            if name.find(".") >= 0:
                file_list.remove(name)
        return file_list

