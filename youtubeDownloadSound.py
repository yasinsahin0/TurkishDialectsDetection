import pandas as pd
import numpy as np
import os

class SoundDownload:

    def __init__(self):
        self.class_column_name = "lehce"
        self.csv_data="youtube_sound_data.csv"
        self.sound_download_file = "sound_download"
        self.main_path = os.getcwd()

    def class_name_file_create(self):
        data = pd.read_csv(self.main_path+"/"+self.csv_data)
        class_count = len(data[self.class_column_name])
        class_name_list = []
        for cls in range(1, class_count):
            class_name = data[self.class_column_name][cls]
            class_name_list.append(class_name)
        for file_name in set(class_name_list):
            os.mkdir(self.main_path + "/" + self.sound_download_file + "/" + file_name)


nesne = SoundDownload()
nesne.class_name_file_create()

