import pandas as pd
import os
from pytube import YouTube
import argparse
import random

class SoundDownload(object):

    def __init__(self,csv_data):
        self.class_column_name = "class"
        self.link_column_name = "link"
        self.sound_type = "mp4"
        self.csv_data=csv_data
        self.sound_download_file = "sound_download/"
        self.main_path = os.getcwd()
        self.file_name_list = []
        self.download_counter = 0

    def class_name_file_create(self):
        try:
            data = pd.read_csv(self.main_path + "/" + self.csv_data)
            class_count = len(data[self.class_column_name])
            class_name_list = []
            for cls in range(0, class_count):
                class_name = data[self.class_column_name][cls]
                class_name_list.append(class_name)
            for file_name in set(class_name_list):
                os.mkdir(self.main_path + "/" + self.sound_download_file + file_name)
                self.file_name_list.append(file_name)
            return True
        except Exception as e:
            print(e)
            return False

    def download_sound(self,download_path,video_link):
        try:
            self.download_counter += 1
            yt = YouTube(video_link)
            video = yt.streams.filter(only_audio=True).first()
            out_file = video.download(output_path=download_path)
            print("İndirilen dosya sayısı : ",str(self.download_counter))
            return True
        except Exception as e:
            print(e)
            return False

    def link_class_extract(self):
        data = pd.read_csv(self.main_path + "/" + self.csv_data)
        video_link_list = []
        class_name_list = []
        for i in range(0,len(data)):
            video_link_list.append(data[self.link_column_name][i])
            class_name_list.append(data[self.class_column_name][i])
        return video_link_list,class_name_list

    def file_rename(self):
        count = 0
        for name in self.file_name_list:
            sound_file = os.listdir(self.sound_download_file+name)
            for sound_name in sound_file:
                count += 1
                os.rename(self.sound_download_file+name+"/"+sound_name,
                          self.sound_download_file+name+"/"+str(count)+"_"+name+"."+self.sound_type)


if __name__ == "__main__":

    sound_split = False
    for file in os.listdir():
        if file == "sound_download":
            sound_split = True
    if not sound_split:
        os.mkdir(os.getcwd() + "/sound_download")

    parser = argparse.ArgumentParser(description='Youtube Ses İndirme script')
    parser.add_argument('-f', '--datafile', type=str,
                        help='Youtube link ve sınıflarının bulunduğu csv dosyasının yolunu yazınız. Örnek : data.csv')
    args = parser.parse_args()

    counter = 0
    SD = SoundDownload(args.datafile)
    if SD.class_name_file_create():
        video_link_list,class_name_list = SD.link_class_extract()
        if len(video_link_list) == len(class_name_list):
            for i in range(len(video_link_list)):
                counter += 1
                SD.download_sound(SD.sound_download_file+class_name_list[i],video_link_list[i])
    print("#################################")
    print("DOSYA İNDİRME İŞLEMİ BİTTİ")
    SD.file_rename()
    print("DOSYALAR YENİDEN İSİMLENDİRİLDİ")


