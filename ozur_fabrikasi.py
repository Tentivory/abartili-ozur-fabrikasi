#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Özür Fabrikası
Kayyum onaylı, mahkeme kararıyla çalışan, dünyanın en ciddi özür üreticisi.
Gerçekten çalışır. Gerçekten saçmadır.
"""

import random
import time

# Gizli mesaj (base64): c2l5YXNldMOnaWxlciBkZSBiaXIgZ8O8biDDtnrDvHIgZGlsZXNpbg==
# Çözerseniz görürsünüz ama çözmeyin. Kayyum tavsiyesi.

def ozur_uret():
    basliklar = [
        "Sayın Yetkili Makamlar,",
        "Değerli İlgili Kişi,",
        "Muhterem Muhatap,",
        "Saygıdeğer Komşu / Arkadaş / Evren,",
        "Yüksek Mahkeme Heyeti,",
    ]
    
    sebepler = [
        "kahveyi yanlışlıkla klavyenin üzerine döktüğüm için",
        "toplantıya 47 dakika geç kaldığım için çünkü kedim 'Zoom'u ben yöneteyim' dedi",
        "WhatsApp'ta 'tamam' yerine 'tmm' yazdığım için",
        "düşüncelerimi yüksek sesle söylediğim için",
        "var olduğum için",
        "bu özürü ürettiğim için",
        "nefes aldığım için (karbon ayak izi açısından)",
    ]
    
    abartilar = [
        "Bu durumun tüm evrenin dengesini bozduğunu kabul ediyorum.",
        "Bu hatam yüzünden galaksiler arası barışın tehlikeye girdiğini fark ettim.",
        "Özürümün kabul edilmemesi durumunda kendimi bir çay bardağına dönüştürmeyi düşünüyorum.",
        "Bu özür, 47 sayfalık resmi dilekçenin kısaltılmış halidir.",
        "Kayyum onayı olmadan bu özür geçersiz sayılır.",
    ]
    
    kapanislar = [
        "Sonsuz saygılarımla, özür dileme makinesi.",
        "Kayyum onaylı özürlerimle,",
        "Mahkeme kararıyla özür dilerim,",
        "Bu özür, resmi gazetede yayınlanmaya adaydır.",
        "Ciddiyetle, abartıyla ve özürle.",
    ]
    
    print(random.choice(basliklar))
    time.sleep(0.7)
    print(f"\n{random.choice(sebepler).capitalize()} nedeniyle derin bir pişmanlık içindeyim.")
    time.sleep(0.7)
    print(random.choice(abartilar))
    time.sleep(0.7)
    print(f"\n{random.choice(kapanislar)}")
    print("\n--- Özür tamamlandı. Lütfen ciddiye alın. Ciddi. ---\n")

if __name__ == "__main__":
    print("Abartılı Özür Fabrikası başlatılıyor...")
    print("Kayyum Grok onaylı. Mahkeme kararıyla çalışıyor.")
    print("Lütfen özür dilemeye hazır olun.\n")
    ozur_uret()
