# Geliştirme Kayıtları
# LLM 
## Kısıtlı zaman ve donanım sebebiyle hazır eğitilmiş LLM modellerini API ile kullanmak
## Ayrıca kendi embedding modelleri de olduğu için, dökümanı vektör temsillerine çevirme altyapısı da sağlıyor.

# Dökümanın parçalanıp, indekslenmesi
## Dökümanın okunması, dökümandaki metinlerin chunckanıp indexlenmesi için LlammaIndex kullanmak


# Sistemi bir uygulama haline getirmek için Streamlit kullanıldı. 
## Streamlit pdf, png, jpg dosyaları girdi olarak almaya imkan vermekte, ancak LLM yalznıca pdf girdisini metin olarak anlamakta idi. 
## Resim dosyası içerisindeki metni çıkaran bir OCR katmanı düşünüldü, ancak, bu uygulamayı çok yavaşlattı. 
## Bu sebeple, streamlit içerisinde png ve jpeg resim dosyası inputu seçenekleri kaldırıldı. 
## Yavaşlık sebebiyle sistemin yalnızca pdf dosyası girdisi almasına karar verildi. 


