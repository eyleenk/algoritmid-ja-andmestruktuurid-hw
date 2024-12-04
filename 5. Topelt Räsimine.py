def räsifn_1(võti, tabeli_suurus):
    return (2 * võti + 3) % tabeli_suurus

def räsifn_2(võti, tabeli_suurus):
    return (3 * võti + 1) % tabeli_suurus

def kokkupõrge(räsitabel, võtmed, tabeli_suurus, räsifn_1, räsifn_2):
    for võti in võtmed:
        index = räsifn_1(võti, tabeli_suurus)
        if not räsitabel[index]:  
            räsitabel[index] = võti
        else:  # topelt-räsi
            nihe = räsifn_2(võti, tabeli_suurus)
            sisestatud = False
            proovide_arv = 1  
            while proovide_arv < tabeli_suurus:
                uus_index = (index + nihe * proovide_arv) % tabeli_suurus
                proovide_arv += 1
                print('Sisestamine {}, proovide arv: {}'.format(võti, proovide_arv))
                if not räsitabel[uus_index]:
                    räsitabel[uus_index] = võti
                    sisestatud = True
                    break
            if not sisestatud:
                print('Ei saa sisestada {}'.format(võti))

def testi_topelt_räsi():
    tabeli_suurus = 11
    räsitabel = [None] * tabeli_suurus
    võtmed = [3, 2, 9, 6, 11, 13, 7, 1, 12, 22]
    kokkupõrge(räsitabel, võtmed, tabeli_suurus, räsifn_1, räsifn_2)
    
    print('Hajutustabel:')
    for i, väärtus in enumerate(räsitabel):
        if väärtus is not None:
            print(f'index {i}: {väärtus}')
        else:
            print(f'index {i}: Tühi')

if __name__ == "__main__":
    testi_topelt_räsi()

#1. Vähendab kokkupõrgete arvu sellega, et on topeltkontroll teise räsifuntskiooni näol. Kui esimene räsifunktsioon põhjustab
# kokkupõrke, siis kasutatakse teist räsifunktsiooni, et leida uus indeks, kuhu võti paigutada. Samuti aitab ühtlustada hajutustabelit
# vähendades cluster'ite teket (järjestikulised tabeli lahtrid mis on andmetega täidetud). Tänu sellele paraneb ka jõudlus. 

#2. Ajakompleksus parimal juhul (kui kokkupõrkeid ei teki) O(1), 
# halvimal juhul (kui tuleb läbi käia kogu tabel ja tekivad cluster'id) O(n). 
# Ruumikompleksus O(n). 

#3 Paku välja stsenaarium, kus topelt räsimine oleks eriti efektiivne.
# Kui peab salvestama paroole andmebaasi.