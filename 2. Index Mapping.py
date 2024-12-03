def index_mapping(arr):
    if not arr:
        raise ValueError("Massiiv ei tohi olla tühi")   
    if not all(isinstance(num, int) for num in arr):
        raise ValueError("Kõik väärtused peavad olema täisarvud")  
    max_väärtus = max(arr)
    indeks = [0] * (max_väärtus + 1)
    for num in arr:
        indeks[num] += 1
    return indeks

# Test
try:
    arr = [1, 3, 2, 3, 4, 1, 6]
    indeks = index_mapping(arr)
    print(indeks)
except ValueError as e:
    print(e)

#Ajakeerukus= O(n) või sama suur, kui suurim väärtus massiivis, kuna peab läbima kõik elemendid ja indeksid.
#Töötab paremini väiksemate andmehulkade puhul, kuna suurte andmehulkade puhul võib indeksite massiiv 
# olla ebaefektiivselt suur.
# Ruumikasutus= peab looma massiivi suurusega max_väärtus + 1, kus max_väärtus on suurim väärtus massiivis.
#Halvimal juhul on väärtuste vahemik liiga suur (1-1000000) ja sel juhul võib ka ruumi kasutus olla liiga suur.

#Reaalses elus saaks rakendada näiteks arvude sageduse leidmiseks või suurte andmete väiksemaks tegemiseks.
#Samuti saab kasutada kui on vaja leida korduvaid arve või unikaalseid arve.
