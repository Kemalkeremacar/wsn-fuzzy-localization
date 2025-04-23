# Kablosuz Sensör Ağlarında Düğüm Lokalizasyonu için Bulanık Mantık Yaklaşımı

## Proje Ekibi
- KEMAL KEREM ACAR - 21360859004
- AHMET ENES YENSİZ - 203608036

## Giriş
Bu projede, Kablosuz Sensör Ağlarında (WSN) düğüm lokalizasyonu problemi için bulanık mantık tabanlı bir yaklaşım geliştirilmiştir. Düğüm lokalizasyonu, WSN'lerde toplanan verilerin anlamlı olabilmesi için kritik öneme sahiptir. Geliştirilen sistem, çapa düğümü oranı, iletim menzili, düğüm yoğunluğu ve yineleme sayısı gibi parametreleri kullanarak Ortalama Lokalizasyon Hatasını (ALE) tahmin etmektedir.

## Veri Seti
Projede kullanılan veri seti, UCI Machine Learning Repository'den alınmıştır. Veri seti, Monte Carlo simülasyonları ile oluşturulmuş olup aşağıdaki özellikleri içermektedir:

- Çapa Düğümü Oranı (anchor_ratio): Toplam düğüm sayısına göre çapa düğümlerinin oranı
- İletim Menzili (trans_range): Düğümlerin iletişim menzili
- Düğüm Yoğunluğu (node_density): Birim alandaki düğüm sayısı
- Yineleme Sayısı (iterations): Lokalizasyon algoritmasının yineleme sayısı
- Ortalama Lokalizasyon Hatası (ale): Hedef değişken
- Standart Sapma (sd_ale): ALE'nin standart sapması

## Metodoloji
### Bulanık Mantık Sistemi
Mamdani tipi bulanık çıkarım sistemi kullanılmıştır. Sistem, dört giriş ve bir çıkış değişkeninden oluşmaktadır:

Giriş Değişkenleri:
1. Çapa Oranı (0-100)
2. İletim Aralığı (0-50)
3. Düğüm Yoğunluğu (0-500)
4. Yineleme (0-100)

Çıkış Değişkeni:
- ALE (0-5)

İki farklı üyelik fonksiyonu tipi test edilmiştir:
1. Üçgen Üyelik Fonksiyonları
2. Gaussian Üyelik Fonksiyonları

Her bir değişken için dilsel terimler:
- Çapa Oranı: {Çok Düşük, Düşük, Orta, Yüksek, Çok Yüksek}
- İletim Aralığı: {Çok Kısa, Kısa, Orta, Uzun, Çok Uzun}
- Düğüm Yoğunluğu: {Çok Az, Az, Orta, Çok, Çok Fazla}
- Yineleme: {Çok Az, Az, Orta, Çok}
- ALE: {Çok Düşük, Düşük, Orta, Yüksek, Çok Yüksek}

### Bulanık Kurallar
Sistem için toplam 13 kural tanımlanmıştır. Örnek kurallar:
1. EĞER (çapa_orani ÇOK_YÜKSEK) VE (iletim_araligi ÇOK_UZUN) VE (dugum_yogunlugu ÇOK_FAZLA) VE (yineleme ÇOK) İSE (ale ÇOK_DÜŞÜK)
2. EĞER (çapa_orani DÜŞÜK) VE (iletim_araligi KISA) VE (dugum_yogunlugu AZ) VE (yineleme ÇOK_AZ) İSE (ale ÇOK_YÜKSEK)

## Sonuçlar ve Tartışma

### Performans Metrikleri
İki farklı üyelik fonksiyonu tipi ve iki farklı berraklaştırma metodu test edilmiştir:

1. Üçgen Üyelik Fonksiyonları:
   - MAE: 2.3942
   - RMSE: 2.4350

2. Gaussian Üyelik Fonksiyonları:
   - MAE: 1.8538
   - RMSE: 1.9059

Berraklaştırma metodunun (centroid vs weighted_average) sonuçlar üzerinde önemli bir etkisi gözlenmemiştir.

### Analiz
- Gaussian üyelik fonksiyonları, üçgen üyelik fonksiyonlarına göre daha iyi performans göstermiştir.
- MAE ve RMSE değerleri arasındaki küçük fark, tahmin hatalarının nispeten dengeli dağıldığını göstermektedir.
- Berraklaştırma metodunun sonuçlar üzerinde etkisinin olmaması, sistemin kararlı olduğunu göstermektedir.

### İyileştirme Önerileri
1. Üyelik fonksiyonlarının parametreleri optimize edilebilir
2. Kural tabanı genişletilebilir
3. Farklı bulanık çıkarım sistemleri (örn. Sugeno) test edilebilir
4. Giriş değişkenlerinin normalizasyonu için farklı yöntemler denenebilir

## Kaynaklar
1. UCI Machine Learning Repository: Wireless Indoor Localization Data Set
2. Zadeh, L.A. (1965). Fuzzy sets. Information and Control, 8(3), 338-353.
3. Mamdani, E.H., & Assilian, S. (1975). An experiment in linguistic synthesis with a fuzzy logic controller. International Journal of Man-Machine Studies, 7(1), 1-13. 