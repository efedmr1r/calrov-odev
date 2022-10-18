# **CALROV Eğitim Sonrası Ödev**


ROS üzerinden python ile ufak bir yapay zekayla görüntü işleme projesi yapmanızı istiyoruz. 

## Yapmanız gerekenler

1. Yeni bir ROS paketi oluşturun.
2. Pakette 2 tane node'unuz olacak.
3. ilk node görüntüyü okuyacak ve bir topice atacak 2. node ise bu topicten görüntüyü alıp görüntü üzerinde yapay zeka ile algılama yapacak. Ardından elde edilen kutuları başka bir topic'e gönderecek.


## Kullanmanız gerekenler
opencv ve tabi ki ROS


### Görüntü için;
yine opencv ile bir node'dan görüntüyü okuyabilirsiniz.
Repository'de 8 tane örnek fotoğraf var. Onları sırayla okuyup işlemenizi istiyoruz.


### Yapay zeka için;
bu repository'de bulunan coco yolov4 modelini kullanacaksınız. Algılama yapmak için opencv dnn modülünü kullanabilirsiniz.
(gpu ile hiç uğraşmayın direkt cpu'dan yapsanız yeter)


### Topicleri oluşturma
görüntüyü aktaracak topic için opencv_bridge adlı ros paketini kullanmanız lazım. ROS sitesinde tutorial'ları var indirip oradan öğrenebilirsiniz.

yapay zeka boxları topici içinse eğitimde gösterdiğimiz gibi kendiniz custom bir mesaj oluşturabilirsiniz.

bu mesajda class_id'ler, score'lar ve box'ları oluşturun


## Ödevi gönderme
Kendinize bir github hesabı açın ve bu git reposunun bir fork'unu oluşturun. Yaptıklarınızı da fork üzerinden yapın. Ödevi teslim etmek içinse bu repoya pull request atın.


### Bonus Görev:
Objeleri tespit ettikten sonra opencv'den yararlanarak resimlerin üzerine detection kutularını çizip yeni resmi bir dosyaya kaydedebilirsiniz.
yapay zekanın döndürdüğü kutular (sol x kordinatı) (üst y kordinatı) (kutunun genişliği) (kutunun yüksekliği) şeklinde oluyor.


### Dipnot 1:
Ödev zorunlu değil ama takıma girmeniz açısından faydalı olacak :)
Takıldığınız noktaları attığımız kaynaklardan veya genel olarak internetten araştırabilirsiniz.

### Dipnot 2:
Yukarıdakilerin tamamını yapmaya çalışın ama yapamazsanız da yapabildiğiniz kadarını gönderin.
Örneğin cv_bridge'i yapamadınız aynı node'dan görüntüyü alıp yapay zekaya atıp öyle box oluşturabilirsiniz. vs vs

### Ödevin Teslimi 25 Ekim

