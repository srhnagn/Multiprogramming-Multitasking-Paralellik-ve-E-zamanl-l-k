import time
import os
import threading
from multiprocessing import Process
import amdahl # Amdahl modulunu buraya dahil ediyoruz

# ==========================================
# 1. BOLUM: COKLU PROGRAMLAMA (Threading)
# ==========================================
def program1():
    for i in range(5):
        print(f"Program 1 calisiyor: {i}")
        time.sleep(1) # Gecikme simulasyonu

def program2():
    for i in range(5):
        print(f"Program 2 calisiyor: {i}")
        time.sleep(1)

def calistir_coklu_programlama():
    print("\n--- 1. COKLU PROGRAMLAMA (THREADING) BASLIYOR ---")
    print("Aciklama: Ayni islemci uzerinde zaman paylasimi yapiliyor.\n")
    
    t1 = threading.Thread(target=program1)
    t2 = threading.Thread(target=program2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(">>> Coklu Programlama Tamamlandi!\n")


# ==========================================
# 2. BOLUM: COKLU ISLEMCI (Multiprocessing)
# ==========================================
def islem_yap(sayi):
    pid = os.getpid()
    kare = sayi * sayi
    print(f"Islemci (PID: {pid}) - Sayi: {sayi}, Kare: {kare}")
    time.sleep(1) 

def calistir_coklu_islemci():
    print("\n--- 2. COKLU ISLEMCI (MULTIPROCESSING) BASLIYOR ---")
    print("Aciklama: Her islem farkli bir cekirdekte/PID ile calisir.\n")
    
    sayilar = [1, 2, 3, 4, 5]
    islemler = []

    for sayi in sayilar:
        p = Process(target=islem_yap, args=(sayi,))
        islemler.append(p)
        p.start()

    for p in islemler:
        p.join()
        
    print(">>> Coklu Islemci Tamamlandi!\n")


# ==========================================
# 3. BOLUM: KARSILASTIRMA (Comparison)
# ==========================================
def kare_hesapla_detayli(sayi, tur):
    pid = os.getpid()
    tid = threading.get_ident()
    print(f"[{tur}] PID: {pid} | Thread ID: {tid} | Sayi: {sayi} -> {sayi*sayi}")
    time.sleep(0.5)

def calistir_karsilastirma():
    print("\n--- 3. KARSILASTIRMA MODU ---")
    sayilar = [1, 2, 3]

    # A) Thread ile
    print("\n[A] Thread (Is Parcacigi) ile calisiyor:")
    threads = []
    for s in sayilar:
        t = threading.Thread(target=kare_hesapla_detayli, args=(s, "THREAD"))
        threads.append(t)
        t.start()
    for t in threads: t.join()

    # B) Process ile
    print("\n[B] Process (Islem) ile calisiyor:")
    procs = []
    for s in sayilar:
        p = Process(target=kare_hesapla_detayli, args=(s, "PROCESS"))
        procs.append(p)
        p.start()
    for p in procs: p.join()
    
    print("\n>>> Karsilastirma Tamamlandi!")


# ==========================================
# ANA MENU
# ==========================================
if __name__ == "__main__":
    # macOS'te multiprocessing hatasini onlemek icin bu blok zorunludur.
    while True:
        print("\n==================================")
        print("   ISLETIM SISTEMLERI ODEVI")
        print("==================================")
        print("1. Coklu Programlama (Threading)")
        print("2. Coklu Islemci (Multiprocessing)")
        print("3. Karsilastirma")
        print("4. Amdahl Yasasi Hesaplayici")
        print("5. Cikis")
        
        secim = input("Seciminiz (1-5): ")

        if secim == '1':
            calistir_coklu_programlama()
        elif secim == '2':
            calistir_coklu_islemci()
        elif secim == '3':
            calistir_karsilastirma()
        elif secim == '4':
            # amdahl.py dosyasindaki fonksiyonu cagiriyoruz
            if 'amdahl' in globals():
                 amdahl.hesapla()
            else:
                 print("Hata: amdahl.py dosyasi bulunamadi!")
        elif secim == '5':
            print("Cikis yapiliyor...")
            break
        else:
            print("Gecersiz secim!")