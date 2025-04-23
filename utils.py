import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def ciz_uyelik_fonksiyonlari(sistem, degisken_adi, baslik):
    """Bir değişkenin üyelik fonksiyonlarını çizer."""
    plt.figure(figsize=(10, 6))
    sistem[degisken_adi].view()
    plt.title(baslik)
    plt.show()

def ciz_tahmin_karsilastirma(gercek, tahmin, baslik):
    """Gerçek ve tahmin değerlerini karşılaştıran bir grafik çizer."""
    plt.figure(figsize=(12, 6))
    plt.scatter(range(len(gercek)), gercek, label='Gerçek Değerler', alpha=0.5)
    plt.scatter(range(len(tahmin)), tahmin, label='Tahmin Değerleri', alpha=0.5)
    plt.title(baslik)
    plt.xlabel('Örnek Indeksi')
    plt.ylabel('ALE Değeri')
    plt.legend()
    plt.show()

def kaydet_sonuclar(sonuclar, dosya_adi='sonuclar.csv'):
    """Sonuçları CSV dosyasına kaydeder."""
    df_sonuclar = pd.DataFrame.from_dict(sonuclar, orient='index')
    df_sonuclar.to_csv(dosya_adi)
    print(f"Sonuçlar {dosya_adi} dosyasına kaydedildi.")

def ciz_sonuclar_karsilastirma(sonuclar):
    """Farklı kombinasyonların sonuçlarını karşılaştıran bir grafik çizer."""
    kombinasyonlar = list(sonuclar.keys())
    mae_values = [sonuclar[k]['MAE'] for k in kombinasyonlar]
    rmse_values = [sonuclar[k]['RMSE'] for k in kombinasyonlar]

    x = np.arange(len(kombinasyonlar))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 6))
    rects1 = ax.bar(x - width/2, mae_values, width, label='MAE')
    rects2 = ax.bar(x + width/2, rmse_values, width, label='RMSE')

    ax.set_ylabel('Hata Değeri')
    ax.set_title('Farklı Kombinasyonların Karşılaştırması')
    ax.set_xticks(x)
    ax.set_xticklabels(kombinasyonlar, rotation=45)
    ax.legend()

    fig.tight_layout()
    plt.show() 