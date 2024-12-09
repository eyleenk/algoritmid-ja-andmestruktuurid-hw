class Sõlm:
    def __init__(self, väärtus):
        self.väärtus = väärtus
        self.vasak = None
        self.parem = None

class Binaarpuu:
    def __init__(self):
        self.juursõlm = None

    def lisa(self, väärtus):
        if self.juursõlm is None:
            self.juursõlm = Sõlm(väärtus)
        else:
            self._lisa(self.juursõlm, väärtus)

    def _lisa(self, praegune_sõlm, väärtus):
        if väärtus < praegune_sõlm.väärtus:
            if praegune_sõlm.vasak is None:
                praegune_sõlm.vasak = Sõlm(väärtus)
            else:
                self._lisa(praegune_sõlm.vasak, väärtus)
        elif väärtus > praegune_sõlm.väärtus:
            if praegune_sõlm.parem is None:
                praegune_sõlm.parem = Sõlm(väärtus)
            else:
                self._lisa(praegune_sõlm.parem, väärtus)
        else:
            print(f"Väärtus {väärtus} on juba puus olemas.")

    def järjesta(self):
        tulemus = []
        self._järjesta(self.juursõlm, tulemus)
        return tulemus

    def _järjesta(self, praegune_sõlm, tulemus):
        if praegune_sõlm:
            self._järjesta(praegune_sõlm.vasak, tulemus)
            tulemus.append(praegune_sõlm.väärtus)
            self._järjesta(praegune_sõlm.parem, tulemus)

    def otsi(self, väärtus):
        return self._otsi(self.juursõlm, väärtus)

    def _otsi(self, praegune_sõlm, väärtus):
        if praegune_sõlm is None:
            return False
        if praegune_sõlm.väärtus == väärtus:
            return True
        if väärtus < praegune_sõlm.väärtus:
            return self._otsi(praegune_sõlm.vasak, väärtus)
        return self._otsi(praegune_sõlm.parem, väärtus)
        
# Testimine
puu = Binaarpuu()
puu.lisa(10)
puu.lisa(5)
puu.lisa(15)
puu.lisa(2)
puu.lisa(7)

print("Järjestatud väärtused:", puu.järjesta())  # Output: [2, 5, 7, 10, 15]
print("Kas 7 on puus?", puu.otsi(7))  # Output: True
print("Kas 20 on puus?", puu.otsi(20))  # Output: False