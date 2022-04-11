import os
from pydub import AudioSegment

class SoundSplit:

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






nesne = SoundSplit()
nesne.sound_data_list_create()