# Sound Splitter

Sound splitter script görevi itibari ile belirli klasör yapısında bulunan ses dosyalarını belirtilen saniye boyutunda parçalara ayırmak ve 
bir dosya altında toplamaktır. Bir dosya altında topladıktan sonra bu ses dosyalarının **dosya yolunu** ve **sınıf ismini** tutan bir
**metadata.csv** dosyası oluşturmaktadır. Öncelikle scriptin sağlıklı çalışabilmesi için gerekli olan parametreleri açıklayarak başlamak istiyorum.  
  
## Requirements

1. sound_download >> bu klasör download scripti ile otomatik oluşmaktadır. Bu main dosya altında her bir sınıfın klasörleri oluşmaktadır. 
* ozbekce >> 1.sınıfımın ismi sound_download klasörümün içindeki klasör.
* azerbaycan >> 2.sınıfım 
* turkmence >> 3.sınıfım  
...  
...  
2. Ses dosyalarının ve bulundukları klasörün isim kontrolü:
sınıf klasörlerinin isimleri youtube_data.csv dosyasındaki sınıf ismi ile aynı olmalıdır.


Klasör hiyerarşisi şu şekilde bulunmalıdır;

| path                                       |
|:------------------------------------------:|
| sound_download/ozbekce/1_ozbekce.mp3       |
| sound_download/azerbaycan/2_azerbaycan.mp3 |
| sound_download/ozbekce/3_ozbekce.mp3       |

NOT : Ses dosyalarının başlarında bulunan sayılar değişiklik gösterebilir.Bu durumu dikkate almayın.
İsim formatında bir farklılık yoksa işleme devam edebilirsiniz. Aykırı bir durum görürseniz split işlemini başlatmayınız...

## Splitter start
Ses dosyalarını parçalamak için oluşturulmuş bir scripttir. **Kullanmadan önce requirements başlığındaki adımların
doğru olduğundan emin olun.** Gereklilikler sağlandıktan sonra **soundSplitter** scriptini şu komut ile çalıştırabilirsiniz.

``` 
$ python soundSplitter.py -s 5 -f sound_download/ -t sound_split/

-h : help :örnek kullanımlar
-s : Kesilecek uzunluk saniye cinsinden
-f : Ham ses dosyalarının bulunduğu ana dizin 
-t : Kesme işleminin sonucunda oluşan ses dosyalarının kayıt edileceği klasör

```
# Script Fonksiyonları
## soundFolderList
Fonksiyon ses dosyalarının bulunduğu klasör isimlerinin bir listesini döndürür. Başında '.' bulunan dosyaları
hariç tutar örnek olarak .gitignore, .DS_Store gibi dosyaları listeye dahil etmez.
```python
    self.main_path = os.getcwd() + "/"
    self.sound_folder_path = "sound_download/"
    
    def soundFolderList(self):
        sound_folder_list = os.listdir(self.main_path+self.sound_folder_path)
        for file_name in sound_folder_list:
            if file_name.find(".") > 0:
                sound_folder_list.remove(file_name)
        return sound_folder_list
```
## soundFileList
Fonksiyon parametre olarak ses dosyalarının bulunduğu klasörlerin listesini alır. Klasör isimlerinin bulunduğu
listeyi gerekli işlemlerden geçirdikten sonra başında '.' bulunan dosyaları hariç tutarak klasör içindeki tüm ses dosyalarının
dosya yollarını liste halinde döndürür.
```python
    self.main_path = os.getcwd() + "/"
    self.sound_folder_path = "sound_download/"
    
    def soundFileList(self,folder_list):
        file_list = []
        for folderName in folder_list:
            if folderName[0] != ".":
                fileList = os.listdir(self.main_path+self.sound_folder_path+folderName)
                for fileName in fileList:
                    if fileName[0] != ".":
                        file_list.append(fileName)
        return file_list
```
## fileFolderNameClean
Fonksiyon parametre olarak ses dosyalarının isimlerinin bulunduğu bir liste alır. Temizleme ve ayrıştırma işlemi
yaparak dosyanın ses dosyası olup olmadığını kontrol eder. Eğer dosya bir ses dosyası değilse listeden ismini siler
ve temizleme işlemini bitirir. Temizlenmiş isim listesinin dönüş olarak verir.
```python

    def fileFolderNameClean(self,file_name_list):
        count = 0
        for name in file_name_list:
            if name[-3:] != self.sound_type:
                count += 1
                file_name_list.remove(name)
                print("Problemli {0} adet dosya listeden çıkarıldı.".format(count))
        return file_name_list
```
## segmentationSound
Ses dosyalarının parçalama işlemini yapmaktadır. Parametre olarak **ses dosyasının ismini, başlangıç süresi, bitiş süresi,
kayit edilecek dosya ismini** alır. Parçalama işlemini [Audiosegment](https://audiosegment.readthedocs.io/en/latest/audiosegment.html)
kütüphanesi ile okunan ses dosyasından gerçekleştirir. 
```python
    self.splitter_path = 'sound_split/sounds/'
    start_time = 5
    end_time = 10
    save_name = "1_kazakca_42"

    def segmentationSound(self, sound_name, start_time, end_time, save_name):
        newAudio = AudioSegment.from_mp3(sound_name)
        sound_piece = newAudio[start_time:end_time]
        sound_piece.export(self.splitter_path + save_name + ".mp3", format="mp3")
```
## metaDataSave
Bölümlendirme işlemi yapılan tüm ses dosyalarının **sınıf ismini, dosya ismini** parametre olarak alır. Bu bilgilerin
hepsini metadata.csv dosyası olarak sound_split klasörünün içinde saklar.
```python
    self.main_path = os.getcwd() + "/"
    self.split_folder = "sound_split/"
    class_name = EKSİK
    name = EKSİK
    def metaDataSave(self,class_name,name):
        file = open(self.main_path + self.split_folder + "metadata.txt", "a")
        file.write(name+","+class_name+"\n")
        file.close()
```

## splitSound
Bölme işlemini gerçekleştirmek için ses dosyalarının listesini ve bölünecek saniye (int) değerini giriş olarak alır.
Ses dosyasının bulunduğu list uzun dosya yolundan oluşmaktadır.(örn sound_split/sounds/2_azerbaycan.mp3) Ses dosyasını
okuyabilmek için [Audiosegment](https://audiosegment.readthedocs.io/en/latest/audiosegment.html) kütüphanesi kullanılmıştır. Bu kütüphane sayesinde ses dosyasının süre olarak
uzunluğuda alınabilmektedir. Süre bölümlendirme sürelerini ve diğer yapılandırmaları bittikten sonra kendi içerisinde
**segmentationSound** fonksiyonunu çağırmaktadır. Ses dosyası her bir bölünme anında **metaDataSave** fonksiyonu çağırılarak
kayıt işlemi gerçekleştirilmektedir. Bu fonksiyon sonuçlandırma fonksiyonudur.

```python

    self.main_path = os.getcwd() + "/"
    self.split_folder = "sound_split/"
    second = 4
    file_list = [EKSİK EKSİK]
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
                
        print("Meta Data Oluşturuldu : ",self.main_path + self.split_folder + "metadata.csv")
        os.rename(self.main_path + self.split_folder + "metadata.txt",
                  self.main_path + self.split_folder + "metadata.csv")
        print("Parçalama işlemi başarıyla tamamlandı")
```


## soundFileDataCreate EKSİK
Fonksiyon giriş olarak ses dosyalarının temizlenmiş isimlerinin bulunduğu listeyi alır. Bu fonksiyon scriptin
en son çalışan fonksiyonudur. Bölümleme işlemi bittikten sonra devreye girer ve tüm ayrıştırılan ses dosyalarının
isimlerinin ve sınıflarının bulunduğu bir

```python
    self.main_path = os.getcwd() + "/"
    self.split_folder = "sound_split/"
    
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
```