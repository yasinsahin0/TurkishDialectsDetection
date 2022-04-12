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

### Örnek - youtube_data.csv
| link                         | class      |
| ---------------------------- |:----------:|
| https://youtu.be/c7G_2THFs8Y | ozbekce    |
| https://youtu.be/IgO2Y2fPYPM | azerbaycan |
| https://youtu.be/S2R1T6x8tRw | ozbekce    |

Klasör hiyerarşisi şu şekilde bulunmalıdır;
| path                                       |
| ------------------------------------------ |
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