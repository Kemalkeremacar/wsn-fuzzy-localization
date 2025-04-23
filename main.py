import numpy as np
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error
from utils import ciz_uyelik_fonksiyonlari, ciz_tahmin_karsilastirma, kaydet_sonuclar, ciz_sonuclar_karsilastirma

def yukle_veri():
    """Veri setini yükler ve hazırlar."""
    df = pd.read_csv('mcs_ds_edited_iter_shuffled.csv')
    return df

def olustur_bulanik_sistem(uyelik_tipi='ucgen'):
    """Bulanık mantık sistemini oluşturur."""
    # Giriş değişkenleri
    capa_orani = ctrl.Antecedent(np.arange(0, 101, 1), 'capa_orani')  # 0-100 arası
    iletim_araligi = ctrl.Antecedent(np.arange(0, 51, 1), 'iletim_araligi')  # 0-50 arası
    dugum_yogunlugu = ctrl.Antecedent(np.arange(0, 501, 1), 'dugum_yogunlugu')  # 0-500 arası
    yineleme = ctrl.Antecedent(np.arange(0, 101, 1), 'yineleme')  # 0-100 arası
    
    # Çıkış değişkeni
    ale = ctrl.Consequent(np.arange(0, 5.1, 0.1), 'ale')  # 0-5 arası
    
    # Üyelik fonksiyonlarını oluştur
    if uyelik_tipi == 'ucgen':
        # Üçgen üyelik fonksiyonları - optimize edilmiş parametreler
        capa_orani['cok_dusuk'] = fuzz.trimf(capa_orani.universe, [0, 0, 30])
        capa_orani['dusuk'] = fuzz.trimf(capa_orani.universe, [0, 30, 60])
        capa_orani['orta'] = fuzz.trimf(capa_orani.universe, [30, 60, 90])
        capa_orani['yuksek'] = fuzz.trimf(capa_orani.universe, [60, 90, 100])
        capa_orani['cok_yuksek'] = fuzz.trimf(capa_orani.universe, [90, 100, 100])
        
        iletim_araligi['cok_kisa'] = fuzz.trimf(iletim_araligi.universe, [0, 0, 15])
        iletim_araligi['kisa'] = fuzz.trimf(iletim_araligi.universe, [0, 15, 30])
        iletim_araligi['orta'] = fuzz.trimf(iletim_araligi.universe, [15, 30, 45])
        iletim_araligi['uzun'] = fuzz.trimf(iletim_araligi.universe, [30, 45, 50])
        iletim_araligi['cok_uzun'] = fuzz.trimf(iletim_araligi.universe, [45, 50, 50])
        
        dugum_yogunlugu['cok_az'] = fuzz.trimf(dugum_yogunlugu.universe, [0, 0, 100])
        dugum_yogunlugu['az'] = fuzz.trimf(dugum_yogunlugu.universe, [0, 100, 200])
        dugum_yogunlugu['orta'] = fuzz.trimf(dugum_yogunlugu.universe, [100, 200, 300])
        dugum_yogunlugu['cok'] = fuzz.trimf(dugum_yogunlugu.universe, [200, 300, 400])
        dugum_yogunlugu['cok_fazla'] = fuzz.trimf(dugum_yogunlugu.universe, [300, 400, 500])
        
        yineleme['cok_az'] = fuzz.trimf(yineleme.universe, [0, 0, 25])
        yineleme['az'] = fuzz.trimf(yineleme.universe, [0, 25, 50])
        yineleme['orta'] = fuzz.trimf(yineleme.universe, [25, 50, 75])
        yineleme['cok'] = fuzz.trimf(yineleme.universe, [50, 75, 100])
        
        ale['cok_dusuk'] = fuzz.trimf(ale.universe, [0, 0, 1])
        ale['dusuk'] = fuzz.trimf(ale.universe, [0, 1, 2])
        ale['orta'] = fuzz.trimf(ale.universe, [1, 2, 3])
        ale['yuksek'] = fuzz.trimf(ale.universe, [2, 3, 4])
        ale['cok_yuksek'] = fuzz.trimf(ale.universe, [3, 4, 5])
    else:
        # Gaussian üyelik fonksiyonları - optimize edilmiş parametreler
        capa_orani['cok_dusuk'] = fuzz.gaussmf(capa_orani.universe, 0, 15)
        capa_orani['dusuk'] = fuzz.gaussmf(capa_orani.universe, 30, 15)
        capa_orani['orta'] = fuzz.gaussmf(capa_orani.universe, 60, 15)
        capa_orani['yuksek'] = fuzz.gaussmf(capa_orani.universe, 90, 15)
        capa_orani['cok_yuksek'] = fuzz.gaussmf(capa_orani.universe, 100, 15)
        
        iletim_araligi['cok_kisa'] = fuzz.gaussmf(iletim_araligi.universe, 0, 7)
        iletim_araligi['kisa'] = fuzz.gaussmf(iletim_araligi.universe, 15, 7)
        iletim_araligi['orta'] = fuzz.gaussmf(iletim_araligi.universe, 30, 7)
        iletim_araligi['uzun'] = fuzz.gaussmf(iletim_araligi.universe, 45, 7)
        iletim_araligi['cok_uzun'] = fuzz.gaussmf(iletim_araligi.universe, 50, 7)
        
        dugum_yogunlugu['cok_az'] = fuzz.gaussmf(dugum_yogunlugu.universe, 0, 50)
        dugum_yogunlugu['az'] = fuzz.gaussmf(dugum_yogunlugu.universe, 100, 50)
        dugum_yogunlugu['orta'] = fuzz.gaussmf(dugum_yogunlugu.universe, 200, 50)
        dugum_yogunlugu['cok'] = fuzz.gaussmf(dugum_yogunlugu.universe, 300, 50)
        dugum_yogunlugu['cok_fazla'] = fuzz.gaussmf(dugum_yogunlugu.universe, 400, 50)
        
        yineleme['cok_az'] = fuzz.gaussmf(yineleme.universe, 0, 12)
        yineleme['az'] = fuzz.gaussmf(yineleme.universe, 25, 12)
        yineleme['orta'] = fuzz.gaussmf(yineleme.universe, 50, 12)
        yineleme['cok'] = fuzz.gaussmf(yineleme.universe, 75, 12)
        
        ale['cok_dusuk'] = fuzz.gaussmf(ale.universe, 0, 0.5)
        ale['dusuk'] = fuzz.gaussmf(ale.universe, 1, 0.5)
        ale['orta'] = fuzz.gaussmf(ale.universe, 2, 0.5)
        ale['yuksek'] = fuzz.gaussmf(ale.universe, 3, 0.5)
        ale['cok_yuksek'] = fuzz.gaussmf(ale.universe, 4, 0.5)

    # Genişletilmiş bulanık mantık kuralları
    kurallar = [
        # Çapa oranı yüksek olduğunda
        ctrl.Rule(capa_orani['cok_yuksek'] & iletim_araligi['cok_uzun'] & 
                 dugum_yogunlugu['cok_fazla'] & yineleme['cok'], ale['cok_dusuk']),
        ctrl.Rule(capa_orani['yuksek'] & iletim_araligi['uzun'] & 
                 dugum_yogunlugu['cok'] & yineleme['orta'], ale['dusuk']),
        
        # Çapa oranı orta olduğunda
        ctrl.Rule(capa_orani['orta'] & iletim_araligi['orta'] & 
                 dugum_yogunlugu['orta'] & yineleme['orta'], ale['orta']),
        ctrl.Rule(capa_orani['orta'] & iletim_araligi['kisa'] & 
                 dugum_yogunlugu['az'] & yineleme['az'], ale['yuksek']),
        
        # Çapa oranı düşük olduğunda
        ctrl.Rule(capa_orani['dusuk'] & iletim_araligi['kisa'] & 
                 dugum_yogunlugu['az'] & yineleme['cok_az'], ale['cok_yuksek']),
        ctrl.Rule(capa_orani['cok_dusuk'] & iletim_araligi['cok_kisa'] & 
                 dugum_yogunlugu['cok_az'] & yineleme['cok_az'], ale['cok_yuksek']),
        
        # Özel durumlar
        ctrl.Rule(capa_orani['yuksek'] & dugum_yogunlugu['cok_az'], ale['orta']),
        ctrl.Rule(iletim_araligi['cok_kisa'] & yineleme['cok'], ale['yuksek']),
        ctrl.Rule(iletim_araligi['cok_uzun'] & dugum_yogunlugu['cok_fazla'], ale['dusuk']),
        ctrl.Rule(capa_orani['orta'] & yineleme['cok_az'], ale['orta']),
        ctrl.Rule(dugum_yogunlugu['cok_fazla'] & yineleme['cok'], ale['dusuk']),
        ctrl.Rule(capa_orani['cok_yuksek'] & iletim_araligi['cok_uzun'], ale['cok_dusuk']),
        ctrl.Rule(dugum_yogunlugu['cok_az'] & yineleme['cok_az'], ale['cok_yuksek'])
    ]

    sistem = ctrl.ControlSystem(kurallar)
    simulasyon = ctrl.ControlSystemSimulation(sistem)
    
    return simulasyon

def hesapla_metrikler(gercek, tahmin):
    """MAE ve RMSE metriklerini hesaplar."""
    # NaN değerlerini filtrele
    valid_indices = ~np.isnan(tahmin)
    gercek_filtered = np.array(gercek)[valid_indices]
    tahmin_filtered = np.array(tahmin)[valid_indices]
    
    if len(gercek_filtered) == 0:
        return float('inf'), float('inf')
    
    mae = mean_absolute_error(gercek_filtered, tahmin_filtered)
    rmse = np.sqrt(mean_squared_error(gercek_filtered, tahmin_filtered))
    return mae, rmse

def main():
    # Veriyi yükle
    df = yukle_veri()
    
    # Her kombinasyon için test et
    uyelik_tipleri = ['ucgen', 'gaussian']
    berraklastirma_metodlari = ['centroid', 'weighted_average']
    
    sonuclar = {}
    
    for ut in uyelik_tipleri:
        for bm in berraklastirma_metodlari:
            print(f"\nÜyelik Tipi: {ut}, Berraklaştırma Metodu: {bm}")
            
            # Bulanık sistemi oluştur
            sistem = olustur_bulanik_sistem(ut)
            
            # Tahminleri yap
            tahminler = []
            for _, row in df.iterrows():
                try:
                    sistem.input['capa_orani'] = row['anchor_ratio']
                    sistem.input['iletim_araligi'] = row['trans_range']
                    sistem.input['dugum_yogunlugu'] = row['node_density']
                    sistem.input['yineleme'] = row['iterations']
                    
                    sistem.compute()
                    tahmin = sistem.output['ale']
                    tahminler.append(tahmin)
                except:
                    tahminler.append(np.nan)
            
            # Metrikleri hesapla
            mae, rmse = hesapla_metrikler(df['ale'], tahminler)
            sonuclar[f"{ut}_{bm}"] = {'MAE': mae, 'RMSE': rmse}
            
            print(f"MAE: {mae:.4f}")
            print(f"RMSE: {rmse:.4f}")
            
            # Görselleştirme
            ciz_tahmin_karsilastirma(df['ale'], tahminler, 
                                   f"{ut} Üyelik Fonksiyonu - {bm} Berraklaştırma")
    
    # Sonuçları kaydet ve karşılaştır
    kaydet_sonuclar(sonuclar)
    ciz_sonuclar_karsilastirma(sonuclar)
    
    return sonuclar

if __name__ == "__main__":
    sonuclar = main() 