# Bulanık Mantık ile Kablosuz Sensör Ağlarında Düğüm Lokalizasyonu

Bu proje, Kablosuz Sensör Ağlarında (WSN) düğüm lokalizasyonu problemini Mamdani Bulanık Çıkarım Sistemi kullanarak çözmektedir. Sistem, çeşitli ağ parametrelerine dayanarak Ortalama Lokalizasyon Hatasını (ALE) tahmin etmektedir.
 
## Proje Genel Bakış

Proje, UCI Machine Learning Repository'den alınan bir veri setini kullanarak WSN'lerde lokalizasyon hatalarını tahmin etmek için bir bulanık mantık sistemi geliştirmektedir. Sistem, tahmin doğruluğunu optimize etmek için farklı üyelik fonksiyonları ve berraklaştırma yöntemleri uygulamaktadır.

## Özellikler

- İki farklı üyelik fonksiyonu:
  - Üçgen
  - Gauss
- İki farklı berraklaştırma yöntemi:
  - Toplamların Merkezi
  - Ağırlıklı Ortalama
- Performans metrikleri:
  - Ortalama Mutlak Hata (MAE)
  - Kök Ortalama Kare Hata (RMSE)

## Sonuçlar

| Üyelik Fonksiyonu | Berraklaştırma Yöntemi | MAE    | RMSE   |
|-------------------|------------------------|--------|--------|
| Üçgen             | Toplamların Merkezi    | 2.3942 | 2.4350 |
| Üçgen             | Ağırlıklı Ortalama     | 2.3942 | 2.4350 |
| Gauss             | Toplamların Merkezi    | 1.8538 | 1.9059 |
| Gauss             | Ağırlıklı Ortalama     | 1.8538 | 1.9059 |

## Gereksinimler

- Python 3.x
- Gerekli paketler (`requirements.txt` dosyasında belirtilmiştir):
  - numpy
  - pandas
  - scikit-fuzzy
  - scikit-learn

## Kurulum

1. Depoyu klonlayın:
```bash
git clone https://github.com/yourusername/wsn-fuzzy-localization.git
cd wsn-fuzzy-localization
```

2. Sanal ortam oluşturun ve etkinleştirin:
```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
```

3. Gereksinimleri yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım

1. Ana programı çalıştırın:
```bash
python main.py
```

2. Sonuçlar `sonuclar.csv` dosyasına kaydedilecektir.

## Proje Yapısı

- `main.py`: Ana program dosyası
- `utils.py`: Yardımcı fonksiyonlar
- `requirements.txt`: Proje bağımlılıkları
- `rapor.md`: Proje raporu
- `sunum.md`: Sunum planı

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için LICENSE dosyasına bakınız.

## Teşekkürler

- Veri seti kaynağı: UCI Machine Learning Repository
- Ders: Esnek Hesaplama
- Kurum: Bursa Teknik Üniversitesi
