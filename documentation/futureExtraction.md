
hata 1 : FutureWarning: Pass y=[ 0.          0.          0.         ... -0.03633136 -0.03303773 -0.03676501] as keyword args.
From version 0.10 passing these as positional arguments will result in an error mfcc = librosa.feature.mfcc(data, sr=sample_rate,n_mfcc=40)  
çözüm 1 : mfcc = librosa.feature.mfcc(y=data, sr=sample_rate,n_mfcc=40)  

Uyarı gidermek için : https://docs.python.org/3/library/warnings.html  

hata 2: jupyter notebook içine py dosyası import edilemiyor.
çözüm 2 : https://stackoverflow.com/questions/15514593/importerror-no-module-named-when-trying-to-run-python-script/15622021#15622021
Dosya yolunu belirmek gerekiyor.