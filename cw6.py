tolerancja = 0.1e-4
dolna = 0.0
gorna =2.0
 
srodek = gorna -dolna
 
while srodek > tolerancja:
    srodek=(dolna+gorna)/2
    if srodek **2 <2.0:
       dolna = srodek
    else:
       gorna=srodek
 
    print(dolna, gorna)
    srodek = gorna-dolna
