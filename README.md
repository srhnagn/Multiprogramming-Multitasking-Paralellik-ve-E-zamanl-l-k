# İşletim Sistemleri Ödevi: Multiprogramming, Multiprocessing ve Amdahl Yasası

**Ders:** İşletim Sistemleri (Operating Systems)  

Bu proje, İşletim Sistemleri dersi 10. hafta çalışmaları kapsamında; **Çoklu Programlama (Multiprogramming)**, **Çoklu İşlemci (Multiprocessing)** kavramlarını uygulamalı olarak göstermek ve **Amdahl Yasası** hesaplamalarını yapan bir araç geliştirmek amacıyla hazırlanmıştır.

## 📂 Proje İçeriği

Proje 3 ana modül ve bir hesaplayıcıdan oluşmaktadır:

1.  **Çoklu Programlama (Multiprogramming):**
    * `Threading` kütüphanesi kullanılarak geliştirilmiştir.
    * Tek bir işlemci üzerinde zaman paylaşımı (time-sharing) yapılarak birden fazla iş parçacığının (thread) nasıl eşzamanlı (concurrent) çalıştığı simüle edilmiştir.

2.  **Çoklu İşlemci (Multiprocessing):**
    * `Multiprocessing` kütüphanesi kullanılmıştır.
    * İşlemlerin farklı işlemci çekirdeklerine dağıtılarak (farklı PID'ler ile) gerçek paralel çalışma mantığı gösterilmiştir.

3.  **Karşılaştırma Modu:**
    * Thread ve Process farkını, Process ID (PID) ve Thread ID değerlerini göstererek analiz eden bir modüldür.

4.  **Amdahl Yasası Hesaplayıcı:**
    * Sistemin paralelleştirilebilir oranına ve işlemci sayısına göre teorik maksimum hızlanmayı (Speedup) hesaplayan ve tablo halinde sunan özel bir modüldür.

## 🚀 Kurulum ve Çalıştırma

Proje dosyaları Python dili ile yazılmıştır. Çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1.  Terminal veya Komut İstemi'ni açın.
2.  Dosyaların bulunduğu dizine gidin.
3.  odev.py dosyasını çalıştırın:

```bash
python3 odev.py
