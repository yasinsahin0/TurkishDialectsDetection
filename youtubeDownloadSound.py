import pandas as pd
import numpy as np

class SoundDownload:
    def __init__(self):
        self.class_column_name = "lehce"

    def class_name_create(self):
        data = pd.read_csv("youtube_sound_data.csv")
        class_count = len(data[self.class_column_name])
        class_name_list = []
        for cls in range(1, class_count):
            class_name = data[self.class_column_name][cls]
            class_name_list.append(class_name)
        return set(class_name_list)



