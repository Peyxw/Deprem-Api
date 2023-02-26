# Deprem-Api
Deprem-Api tercihe göre AFAD veya Kandilli Rasatanesi`nin deprem verilerini işliyerek. Türkiye üzerinde olan depremleri JSON formatı üzerinden halka sunar.<br>




## Özellikler
- USGS sistemin kullandığı parametleri kullanır.
- Düzenlene bilir
- Filtreleme yapar
- 1 Dakika aralıklar ile güncellenen deprem verileri.

## Kurulum
```py
pip install gunicorn
pip install schedule
pip install autopep8
pip install beautifulsoup4
pip install flask

```
# Kullanım
Bu kullanım yönergesi kendi bilgisayarınıza kurmanız için oluşturuldu
```py
py index.html

```
Sistem çalıştığı zaman sizlere bir internet adresi verecektir ordan giriş sağlıya bilirsiniz.

###JSON Çıktısı
```json
{
  "type": "FeatureCollection",
  "metadata": {
    "generated": "null",
    "url": "null",
    "title": "PEYXW DEPREM",
    "status": 500,
    "api": "1.0.0",
    "count": 500
  },
  "features": [
    {
      "features": {
        "type": "Feature",
        "properties": {
          "mag": {
            "md": 0,
            "ml": 1.8,
            "mw": 0
          },
          "place": [
            3.1,
            "HACIKODAL-GOKSUN (KAHRAMANMARAS)"
          ],
          "time": 1677371367,
          "updated": 1677371367,
          "tz": "null",
          "url": "null",
          "detail": "null",
          "felt": "null",
          "cdi": "null",
          "mmi": "null",
          "alert": "null",
          "status": "İlksel",
          "tsunami": "0",
          "sig": "0",
          "net": "us",
          "code": 0.11752361851974358,
          "ids": 0.11752361851974358,
          "sources": ",us,",
          "types": ",origin,phase-data,",
          "nst": "0",
          "dmin": "0",
          "rms": "0",
          "gap": "0",
          "magType": "mb",
          "type": "earthquake",
          "title": [
            3.1,
            "HACIKODAL-GOKSUN (KAHRAMANMARAS)"
          ]
        },
        "geometry": "İlksel",
        "coordinates": [
          37.9418,
          36.2945,
          3.1
        ],
        "id": 0.11752361851974358
      }
    },
```


# Destek Talebi
Her hanigi bir sorunuz veya takıldığınız bir yer var ise eminnesatg@gmail.com adresinden bana ulaşa bilir veya bir talep oluştura bilirsiniz.

# Katkı
Katkıda bulunmak için [Burayı](https://opensource.guide/tr/how-to-contribute/) gözden geçirerek katkıda buluna bilirsiniz.

# Yol Haritası
**HER HANGİ BİR YOL HARİTASI BULUNMAMAKTA**
# Lisans
``` 
MIT License

Copyright (c) 2023 Emin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
# Proje durumu
Geliştirilmeye devam ediliyor
