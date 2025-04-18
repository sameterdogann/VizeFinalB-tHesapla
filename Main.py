#-------------------------------------------------------------------------------
# Name:        VizeFinalBüt
# Purpose:     Vize ve final notlarını hesaplayarak bütünlemeye kalınıp kalınmadığını belirler
#
# Author:      Abdul Samet
#
# Created:     18/04/2025
# Copyright:   (c) Abdul Samet 2025
# Licence:     None
#-------------------------------------------------------------------------------

### VİZE FİNAL HESAPLAYARAK BÜT E GİRECEK MİYİM HESAPLAMA
try:
    while True:
        try:
            vize = int(input("Vize notunuzu giriniz (0-100): "))
            final = int(input("Final notunuzu giriniz (0-100): "))
            
            vizeFinalSum = (vize*0.4) + (final*0.6)
            
            if 50 <= vizeFinalSum <= 100:
                print("Bütünlemeye girmene gerek yok. Geçtiniz!")
                break
            elif 0 <= vizeFinalSum < 50:
                print("Bütünlemeye kaldınız.\n")
                
                secim = int(input("Büt notunuz girildiyse 1, girilmediyse 0 giriniz: "))
                if secim == 1:
                    büt_not = int(input("Bütünleme notunuzu giriniz (0-100): "))
                    if (vize*0.4 + büt_not*0.6) >= 50:
                        print("Bütünleme sayesinde geçtiniz!")
                        break
                    else:
                        print("Maalesef bütünleme sonrası da kaldınız.")
                        break
            else:
                print("Notlar 0-100 aralığında olmalıdır!")
                
        except ValueError:
            print("Lütfen sayısal bir değer giriniz!!!")
            
except KeyboardInterrupt:
    print("\nProgram kapatılıyor...")
