import os
import librosa
from pydub import AudioSegment
import argparse

class SoundSplitter:

    def __init__(self):
        self.sound_folder_path = 'sound_download/'
        self.splitter_path = 'sound_split/sounds/'
        self.split_folder = 'sound_split/'
        self.main_path = os.getcwd() + "/"
        self.sound_type = "wav"

    # Ses dosyalarının bulunduğu klasör isimlerinin listesini dönüyor
    def soundFolderList(self):
        sound_folder_list = os.listdir(self.main_path+self.sound_folder_path)
        for file_name in sound_folder_list:
            if file_name.find(".") > 0:
                sound_folder_list.remove(file_name)
        return sound_folder_list

    # Ses dosyalarının isimlerini dönüyor
    def soundFileList(self,folder_list):
        file_list = []
        for folderName in folder_list:
            fileList = os.listdir(self.main_path+self.sound_folder_path+folderName)
            for fileName in fileList:
                file_list.append(fileName)
        return file_list

    # Ses dosyaları listesinin içinde ayrık tipteki dosyaları temizliyor
    def fileFolderNameClean(self,file_name_list):
        count = 0
        for name in file_name_list:
            if name[-3:] != self.sound_type:
                count += 1
                file_name_list.remove(name)
                print("Problemli {0} adet dosya listeden çıkarıldı.".format(count))
        return file_name_list

    # Ses dosyalarının isimleri ve sınıfları için data.csv dosyası oluşturuyor.
    def soundFileDataCreate(self,sound_file_list):
        file = open(self.main_path + self.split_folder + "data.txt", "a")
        file.write("class_name,sound_file_name\n")
        for name in sound_file_list:
            temp_list = name.split("_")
            cls_name = temp_list[1][:-4]
            file_path = self.sound_folder_path + cls_name + "/" + name
            file.write(cls_name + "," + file_path + "\n")
        file.close()
        os.rename(self.main_path + self.split_folder + "data.txt",
                  self.main_path + self.split_folder + "data.csv")

    # Bölme işlemini başlatan fonksiyon, tam dosya yolu bulunan ses dosyalarının listesini ve
    # kaç saniye bölünecek bilgisini alıyor
    def splitSound(self, file_list, second):
        for sound_path in file_list:
            audio = AudioSegment.from_file(sound_path)
            seconds = int(audio.duration_seconds)
            listem = []
            count = 0
            for i in range(0, seconds, second):
                listem.append(i * 1000)
            for a in range(0, len(listem) - 1):
                count += 1
                self.segmentationSound( sound_path,
                                        listem[a],
                                        listem[a + 1],
                                        sound_path.split("/")[2].split(".")[0] + "_" + str(count))
        print("Parçalama işlemi başarıyla tamamlandı")

    # ses dosyalarını bölme işlemini gerçekleştiriyor
    def segmentationSound(self, sound_name, start_time, end_time, save_name):
        newAudio = AudioSegment.from_wav(sound_name)
        sound_piece = newAudio[start_time:end_time]
        sound_piece.export(self.splitter_path + save_name + ".wav", format="wav")


    # Bölümlenmemiş ses dosyalarının tam yolunu tutan bir liste döndürüyor
    def fullSoundPathList(self):
        main_list = []
        folder_list = self.soundFolderList()
        for folder in folder_list:
            for file in os.listdir(self.sound_folder_path+folder):
                main_list.append(self.sound_folder_path+folder+"/"+file)
        return main_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ses bölümleme script')
    parser.add_argument('-s','--second', type=int,
                        help='Ses dosyalarını bölmek istediğiniz saniye değeri')

    args = parser.parse_args()
    if args.second > 0:
        SP = SoundSplitter()
        folder_list = SP.soundFolderList()
        file_list = SP.soundFileList(folder_list)
        clean_file_list = SP.fileFolderNameClean(file_list)
        full_sound_path_list = SP.fullSoundPathList()
        SP.splitSound(full_sound_path_list, args.second)
        SP.soundFileDataCreate(clean_file_list) # Data dosyasını oluşturuyor