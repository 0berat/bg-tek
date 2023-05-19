import random
import time
#Timeri internetten hazir aldim.
class timer:
    def baslat(self):
        self.baslangic = time.perf_counter()

    def bitir(self):
        self.bitis = time.perf_counter()
        fark = (self.bitis-self.baslangic)
        print(f"{fark} saniyede'de tamamlandı.")


timer = timer()

timer.baslat()

#ilk 0 ile 100 arasindan rastgele bir sayi cekiyoruz. Bu ilk kenar oluyor. 

# Geri kalan kismida 2 ye bolucez. ve 3'e bolunmus olucak

#bu yontem 2 nokta alip kenar belirlemekten daha verimli.
x=0
sayac=0
#while daha uygun gozukuyor.
while x < 1000000:
    x+=1
    ilkK = random.uniform(1, 99)
    #print(f'ilk kenar:{ilkK} ')

    araKesim= random.uniform(ilkK,99)

    ikinciK = araKesim - ilkK
    #print(f'ikinci kenar:{ikinciK} ')

    ucunK = 100 - araKesim
    #print(f'ucunu kenar:{ucunK} ')
    
    if  ilkK+ikinciK>ucunK and ilkK+ucunK>ikinciK and ikinciK+ucunK>ilkK:
        sayac+=1

timer.bitir()

print(f'1.000.000 denemeden: {sayac} tanesi ucgen olustu')
basari_orani = sayac/1000000*100
print(f'basari orani :%{basari_orani}')
quit()
