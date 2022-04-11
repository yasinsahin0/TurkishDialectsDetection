# Makine öğrenmesi Türk Lehce tahminlenmesi


## Youtube Sound Download

mac : brew install ffmpeg




## Sound Splitter

Ses dosyalarını parçalamak için oluşturulmuş bir scripttir. Kullanmadan önce sound_download klasörüne   
bölünmemiş uzun sürelere sahip ses dosyalarının hiyerarşik olarak indirilmiş olması gerekmektedir.  
Bu scripti çalıştırmadan önce youtubeDownloadSound scripti çalıştırılmaldır.  
Örnek bir sound_download klasör hiyerarşisi şu şekilde olmalıdır.  
```
sound_download >> klasör
    sınıf1 >> klasör
    sınıf2 >> klasör
    sınıf3 >> klasör
```
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
çözüm : sudo apt-get install ffmpeg  
