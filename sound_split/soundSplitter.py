import os
from pydub import AudioSegment
import argparse
import time

# en son parçalama işlemi 5178 dosya oluştu - 158 dakika sürdü
class SoundSplitter(object):

    def __init__(self,sound_folder_name,split_folder_name):
        self.sound_folder_path = sound_folder_name # 'sound_download/'
        self.splitter_path = 'sound_split/sounds/'
        self.split_folder = split_folder_name #'sound_split/'
        self.main_path = os.getcwd() + "/"
        self.sound_type = "mp3"

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
            if folderName[0] != ".":
                fileList = os.listdir(self.main_path+self.sound_folder_path+folderName)
                for fileName in fileList:
                    if fileName[0] != ".":
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
        print("Data dosyası oluşturuldu : ", str(self.main_path + self.split_folder + "data.csv"))

    # Bölme işlemini başlatan fonksiyon, tam dosya yolu bulunan ses dosyalarının listesini ve
    # kaç saniye bölünecek bilgisini alıyor
    def splitSound(self, file_list, second):
        counter = 0
        for sound_path in file_list:
            audio = AudioSegment.from_file(sound_path)
            seconds = int(audio.duration_seconds)
            listem = []
            count = 0
            for i in range(0, seconds, second):
                listem.append(i * 1000)
            for a in range(0, len(listem) - 1):
                count += 1
                counter += 1
                print("{0} adet dosya oluşturuldu.".format(counter))
                self.segmentationSound( sound_path,
                                        listem[a],
                                        listem[a + 1],
                                        sound_path.split("/")[2].split(".")[0] + "_" + str(count))
                cls_name = sound_path.split("/")[2].split(".")[0].split("_")[1]
                full_name = sound_path.split("/")[2].split(".")[0] + "_" + str(count)+".mp3"
                self.metaDataSave(cls_name,full_name)
        print("Meta Data Oluşturuldu : ",self.main_path + self.split_folder + "Splitmetadata.csv")
        os.rename(self.main_path + self.split_folder + "Splitmetadata.txt",
                  self.main_path + self.split_folder + "Splitmetadata.csv")
        print("Parçalama işlemi başarıyla tamamlandı")

    # ses dosyalarını bölme işlemini gerçekleştiriyor
    def segmentationSound(self, sound_name, start_time, end_time, save_name):
        newAudio = AudioSegment.from_mp3(sound_name)
        sound_piece = newAudio[start_time:end_time]
        sound_piece.export(self.splitter_path + save_name + ".mp3", format="mp3")

    def metaDataSave(self,class_name,name):
        file = open(self.main_path + self.split_folder + "Splitmetadata.txt", "a")
        file.write(name+","+class_name+"\n")
        file.close()


    # Bölümlenmemiş ses dosyalarının tam yolunu tutan bir liste döndürüyor
    def fullSoundPathList(self):
        main_list = []
        folder_list = self.soundFolderList()
        for folder in folder_list:
            if folder[0] != ".":
                for file in os.listdir(self.sound_folder_path+folder):
                    if file[0] != ".":
                        main_list.append(self.sound_folder_path+folder+"/"+file)
        return main_list



if __name__ == "__main__":
    sound_split = False
    for file in os.listdir():
        if file == "sound_split":
            sound_split = True

    if not sound_split:
        os.mkdir(os.getcwd() + "/sound_split")
        os.mkdir(os.getcwd()+"/sound_split/sounds")


    parser = argparse.ArgumentParser(description='Ses bölümleme script')
    parser.add_argument('-s','--second', type=int,
                        help='Ses dosyalarını bölmek istediğiniz saniye değeri')
    parser.add_argument('-f','--soundfolder', type=str,
                        help='bölünecek ses dosyalarının klasörü, örnek : sound_download/')
    parser.add_argument('-t','--splitfolder', type=str,
                        help='Bölünmüş seslerin yükleneceği klasör, örnek : sound_split/')
    args = parser.parse_args()
    if args.second > 0:
        if args.soundfolder[-1] == "/":
            if args.splitfolder[-1] == "/":
                now_time = time.time()
                SP = SoundSplitter(args.soundfolder, args.splitfolder)
                folder_list = SP.soundFolderList()
                file_list = SP.soundFileList(folder_list)
                clean_file_list = SP.fileFolderNameClean(file_list)
                full_sound_path_list = SP.fullSoundPathList()
                SP.splitSound(full_sound_path_list, args.second)
                SP.soundFileDataCreate(clean_file_list) # Data dosyasını oluşturuyor
                end_time = time.time()
                print("Toplam geçen süre {0} saniyedir. ".format(int(end_time-now_time,)))
            else:
                print("Dosya yolu hatası sonuna / koyduğunuzdan emin olun")
        else:
            print("Dosya yolu hatası sonuna / koyduğunuzdan emin olun")
    else:
        print("0 dan büyük bir saniye değeri giriniz.")

