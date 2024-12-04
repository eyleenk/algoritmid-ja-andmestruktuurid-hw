def rehash(vana):
    uus_suurus = len(vana) * 2
    uus_tabel = [None] * uus_suurus
    for i in vana:
        if i is not None:
            index = hash_function_1(i, uus_suurus)
            while uus_tabel[index] is not None:
                index = (index + 1) % uus_suurus
            uus_tabel[index] = i
    return uus_tabel

def hash_function_1(key, table_size):
    return (2 * key + 3) % table_size

# Test
vana = [3, 2, 9, 6, 11, 13, 7, 1, 12, 22]
uus_tabel = rehash(vana)
print('Vana tabel:', vana)
print('Uus tabel:', vana)

#Rehashing on protsess, mille käigus räsitabeli suurust suurendatakse ja kõik 
#olemasolevad elemendid ümber räsitakse uude tabelisse. Seda tehakse tavaliselt 
# siis, kui koormustegur ületab teatud läve.

#Räsitabeli koormustegur näitab tabeli täituvust. Selle arvutamiseks jagatakse
#tabelis olevate elementide arv tabeli suurusega. Kui koormustegur on
#liiga suur on suurem tõenäosus kokkupõrgeteks ja otsingu aeg suureneb. Samuti suureneb
#mälu kasutus. Kui koormustegur on liiga väike, siis toimub mälu raiskamine. Optimaalne
#kasutegur on alla 0.7.

#Rehashing vähendab kokkupõrgete tõenäosust, parandab otsingu aega ja
#tagab mälu optimaalse kasutamise ja ühtlase andmete jaotuse.
# Kõik need tegevused parandavad räsitabeli jõudlust. 
