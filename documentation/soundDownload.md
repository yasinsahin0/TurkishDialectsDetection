# Sound Download

Youtube linkleri aracılığı ile toplamış olduğumuz veri setini bizim yerimize mp3 formatında indirip klasör hiyerarşisi kuran bir scripttir.
Bu script kullanımı için gerekli kütüphaneler haricinde başka bir işlem yapmaya gerek bulunmamaktadır. Topladığımız dataların bulunması
gereken dizin ve örnek datalar alt bölümlerde verilecektir.
  
## Requirements

1. youtube_data.csv adında dataların bulunduğu klasörün ana dizinde bulunması gereklidir.
Örnek data dosyası ve içeriği aşağıda gösterilmiştir.  

| link                         | class      |
| ---------------------------- |:----------:|
| https://youtu.be/c7G_2THFs8Y | ozbekce    |
| https://youtu.be/IgO2Y2fPYPM | azerbaycan |
| https://youtu.be/S2R1T6x8tRw | ozbekce    |


## Download start
Datalarımızı indirmek için scripti çalıştırarak konsol ekranından takibini yapabiliriz.Scripti çalıştırmak için
aşağıdaki komudu yazmanız yeterlidir.

``` 
$ python youtubeDownloadSound.py -f data.csv

-h : help :örnek kullanımlar
-f : Link ve sınıfların bulunduğu data dosyasının yolu

```

# Script Fonksiyonları
## class_name_file_create
Data dosyamızda bulunan sınıflarımızın adında klasörler oluşturmaktadır.
```python
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
```
## download_sound
Data dosyamızda linklerini vermiş olduğumuz videolarını indirme işlemini gerçekleştirmektedir. Parametre olarak
dosyanın indirileceği dizini ve video linkini almaktadır. İndirme işleminden önce ve sonra bekleme süresi eklenmiştir.
Bunun sebebi dosya indirmesinde yaşanabilecek sorunları engellemektir.
```python
    def download_sound(self,download_path,video_link):

        time.sleep(2)
        try:
            self.download_counter += 1
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',}],}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_link])
            print("İndirilen dosya sayısı : ",str(self.download_counter))
            time.sleep(3)
            for i in os.listdir(self.main_path):
                if i[-3:] == "mp3":
                    shutil.move(i,download_path)
                    print("move edildi")
            return True
        except Exception as e:
            print(e)
            return False
```
## link_class_extract
Link ve sınıf isimlerini ayrı listelere böler ve bu listeleri dönüş değeri olarak vermektedir.
```python
    def link_class_extract(self):
        data = pd.read_csv(self.main_path + "/" + self.csv_data)
        video_link_list = []
        class_name_list = []
        for i in range(0,len(data)):
            video_link_list.append(data[self.link_column_name][i])
            class_name_list.append(data[self.class_column_name][i])
        return video_link_list,class_name_list
```
## file_rename
En son çalışan fonksiyon olarak indirilen dosyaların isimlerini yeni formatta değiştirir.Bu fonksiyonun
en son çalışmasının sebebi indirilen dosyanın işlenmesini beklemektir.

```python
    def file_rename(self):
        count = 0
        for name in self.file_name_list:
            sound_file = os.listdir(self.sound_download_file+name)
            for sound_name in sound_file:
                count += 1
                os.rename(self.sound_download_file+name+"/"+sound_name,
                          self.sound_download_file+name+"/"+str(count)+"_"+name+"."+self.sound_type)

```