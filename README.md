# Makine öğrenmesi Türk Lehce tahminlenmesi


## Youtube Sound Download

### [Youtube Sound Download Dökümantasyonu](https://github.com/yasinsahin0/Turk-Lehce-ml-ai/blob/main/documentation/soundDownload.md)

Youtube üzerinden toplamış olduğumuz verilerimizi bu script yardımı ile indirebiliriz. Bütün işlemlerin
en başında gelen scripttir. Link ve sınıflarını topladığımız csv dosyamızı girdi olarak veriyoruz.
Detaylı bilgi için dökümantasyonuna gidebilirsiniz.

``` 
$ python youtubeDownloadSound.py -f data.csv

-h : help :örnek kullanımlar
-f : Link ve sınıfların bulunduğu data dosyasının yolu

```

## Sound Splitter

### [Sound Splitter Dökümantasyonu](https://github.com/yasinsahin0/Turk-Lehce-ml-ai/blob/main/documentation/soundSplitter.md)
Ses dosyalarını parçalamak için oluşturulmuş bir scripttir. Kullanmadan önce sound_download klasörüne
bölünmemiş uzun sürelere sahip ses dosyalarının hiyerarşik olarak indirilmiş olması gerekmektedir.
Bu scripti çalıştırmadan önce youtubeDownloadSound scripti çalıştırılmaldır.
[Youtube Download](https://github.com/yasinsahin0/Turk-Lehce-ml-ai/blob/main/documentation/soundDownload.md)
Bu dizinler ve içerinde ses dosyaları olduğundan emin olduktan sonra **soundSplitter**
scriptini şu komut ile çalıştırabilirsiniz.

``` 
python soundSplitter.py -s 5 -f sound_download/ -t sound_split/

-s : Kesilecek uzunluk saniye cinsinden
-f : Ham ses dosyalarının bulunduğu ana dizin
-t : Kesme işleminin sonucunda oluşan ses dosyalarının kayıt edileceği klasör

```

## Hatalar

Hata : youtube_dl.utils.PostProcessingError: ffprobe/avprobe and ffmpeg/avconv not found. Please install one.   
çözüm linux: sudo apt-get install ffmpeg   
çözüm mac : brew install ffmpeg  