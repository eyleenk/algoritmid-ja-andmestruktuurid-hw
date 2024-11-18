# 1)Linear search rakendamine
def lineaarotsing(arr, target):
    for i in range(len(arr)):
        if massiiv[i] == otsitav:
            return i
    return -1
#Test
massiiv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
otsitav = 5
tulemus = lineaarotsing(massiiv, otsitav)
print("Otsitav element on indeksiga", tulemus)

# 2) Aja ja ruumikomplekssus
# Aja komplekssus HALVIMAL juhul O(n), kui otsitavat pole massiivis või see on massiivi viimane element
# KESKMISEL juhul O(n/2) kui element massiivi keskel
# PARIMAL juhul O(1) kui otsitav element on massiivi esimene element

# Ruumikomplekssus O(1) kuna kasutatakse lisamälu

# 3) Kuidas kasutada reaalmaailmas
# Saaks kasutada konkreetse väärtuse otsimiseks suuremast massiivist, nt sõnaraamatust konkreetse sõna või listist teatud arvu otsimiseks.
# Efektiivseim väikeste listide puhul, võivad olla sorteerimata.
# Ei ole kõige efektiivsem suurte listide puhul, kuna aja komplekssus on halvimal juhul O(n), 
# ehk siis kui otsitav element on massiivi viimane element, siis peab kõik elemendid läbi käima.

