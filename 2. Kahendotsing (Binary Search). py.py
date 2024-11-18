def binaarotsing (massiiv, otsitav):
    vasak,parem = 0, len(massiiv)-1 #otsitav vahemik
    while vasak <= parem: #kuni vasak on väiksem või võrdne paremaga
        keskmine = (vasak+parem)//2 #leiame keskmise
        if massiiv[keskmine] == otsitav: #kui keskmine ongi otsitav
            return keskmine #tagastame keskmise
        elif massiiv[keskmine] < otsitav: #kui keskmine on väiksem kui otsitav
            vasak = keskmine + 1 #otsime paremalt poolt
        else:
            parem = keskmine - 1 #kui keskmine on suurem kui otsitav, siis otsime vasakult poolt
    return -1 #kui pole massiivis

#Test
massiiv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
otsitav = 5
tulemus = binaarotsing(massiiv, otsitav)
if tulemus != -1:
    print(f"Element {otsitav} leiti indeksil: {tulemus}")
else:
    print(f"Elementi {otsitav} ei leitud massiivist")

# 2) Võrrelge teoreetilises analüüsis valminud Binary Search'i ja Linear Search'i aegkomplekssust.
# Ajakompleksus on binaarotsingul O(log n) ja lineaarotsingul O(n). 
# Binaarotsing on poole kiirem, kuna jagab listi pooleks. Lineaarotsing otsib iga elementi ükshaaval.
# Lineaarotsingu puhul sõltub otsitava elemendi leidmine sellest, kus see asub. Kui element on massiivi alguses, siis on otsimiseks vaja ainult ühte sammu. 
# Kui element on massiivi lõpus, siis on vaja läbida kõik liikmed. Näiteks 100 elemendiga massiivi puhul on vaja teha halvimal juhtul lineaarotsingu puhul 100 sammu.
# Binaarotsingu puhul on vaja kõige rohkem log2(100) sammu, et leida element. Näiteks 100 elemendiga massiivi puhul on vaja kõige rohkem 7 sammu, et leida element.

# 3) Tooge näide stsenaariumist, kus Binary Search on kasulikum kui Linear Search, ja selgitage miks.
# Näiteks kui on vaja leida mingi element suurest massiivist, siis binaarotsing on kasulikum kui lineaarotsing.
# nt. võrdlus e-poe hindadega, mis on sorteeritud nimekirjas. kui otsida toodet, mille väärtus on täpselt 10 
# eurot, siis binaarotsing leiab selle kiiremini kui lineaarotsing, kuna lineaarotsing taaskord läbib kõik liikmed, ning mida rohkem tooteid, seda aeglasem see on.
# Binaarotsing aga alustab keskelt ning siis vaatab, kas suurus, mida otsitakse, on suurem või väiksem kui keskmine element ja otsib siis sealt.

