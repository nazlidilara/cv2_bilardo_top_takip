# Bilardo Top Takibi Projesi

Proje Açıklaması
Bu proje, OpenCV kullanılarak video akışındaki kırmızı bilardo toplarını tespit eden ve işaretleyen bir Python uygulamasıdır.
Özellikler

Kırmızı renkli topların gerçek zamanlı tespiti
Gaussian bulanıklaştırma ile gürültü azaltma
Morfolojik operasyonlarla görüntü iyileştirme
Topların merkez koordinatlarını ve yarıçapını belirleme

Gereksinimler

Python 3.x
OpenCV (cv2)
NumPy

Kurulum

Gerekli kütüphaneleri yükleyin:

bashCopypip install opencv-python numpy
Kullanım

Video dosya yolunu process_video() fonksiyonunda güncelleyin
Projeyi çalıştırın:

bashCopypython bilardo_top_takibi.py

Çıkış için 'q' tuşuna basın

Algoritma Detayları

HSV renk uzayında kırmızı renk filtrelemesi
Görüntü bulanıklaştırma
Morfolojik operasyonlar
Kontur tespiti ve filtreleme
