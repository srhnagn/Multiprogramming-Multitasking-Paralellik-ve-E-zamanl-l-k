# Dosya Adi: amdahl.py

def hesapla():
    print("\n==================================")
    print("   AMDAHL YASASI HESAPLAYICI")
    print("==================================")
    print("Formul: Speedup = 1 / ((1 - P) + (P / N))")
    print("P: Paralelelestirilebilir kisim orani")
    print("N: Islemci Sayisi\n")

    try:
        p_yuzde = float(input("Paralellestirilebilir kisim orani (% kac? Orn: 60): "))
        p = p_yuzde / 100.0
        
        if not (0 <= p <= 1):
            print("Hata: Oran 0 ile 100 arasinda olmalidir.")
            return

        # Kullanicidan spesifik islemci sayisi al
        n_input = int(input("Hesaplanacak Islemci Sayisi (N): "))
        if n_input < 1:
            print("Hata: Islemci sayisi en az 1 olmalidir.")
            return

        speedup_user = 1 / ((1 - p) + (p / n_input))
        print(f"\n>>> SONUC: {n_input} islemci ile Hizlanma (Speedup): {speedup_user:.2f}x")

        # Tablo Dokumu
        print("\n--- Farkli Islemci Sayilarina Gore Analiz Tablosu ---")
        print(f"{'Islemci (N)':<15} | {'Hizlanma (Speedup)':<20} | {'Verimlilik':<15}")
        print("-" * 55)
        
        test_degerleri = [1, 2, 4, 8, 16, 32, 64, 128, n_input]
        test_degerleri = sorted(list(set(test_degerleri))) 

        for n in test_degerleri:
            speedup = 1 / ((1 - p) + (p / n))
            efficiency = speedup / n 
            print(f"{n:<15} | {speedup:<20.2f}x | {efficiency:.2f}")
            
    except ValueError:
        print("Hata: Lutfen gecerli sayisal degerler girin!")
    
    input("\nDevam etmek icin Enter'a basin...")

if __name__ == "__main__":
    hesapla()