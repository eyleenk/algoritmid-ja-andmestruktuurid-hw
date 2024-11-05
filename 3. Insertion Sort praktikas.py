def insertion_sort(arr): #defineerib funktsiooni
    for i in range(1, len(arr)): #iga liikme kohta alates 1 (mitte 0, kuna esimest elementi loetakse juba sorteerituks) kuni loendi pikkuseni,
        key = arr[i] #määratakse praeguse elemendi väärtus, mida hakatakse võrdlema
        j = i - 1 #asetab j väärtuse eelmisele kohale, ehk alustab elemendi võrdlemist eelmise elemendiga loendis
        while j >= 0 and key < arr[j]: #töötab, kuni j on suurem või võrdne 0 ja key on väiksem kui arr[j]
            arr[j + 1] = arr[j] #kui key väärtus on väiksem, kui arr[j], siis liigutatakse ta ühe võrra paremale
            j -= 1 #j väheneb ühe võrra
        arr[j + 1] = key #kui key pole enam väiksem, kui arr, tõstetakse j väärtus ühe võrra tagasi, ehk oma algsele kohale

# test
arr = [12, 11, 13, 5, 6, 7]
insertion_sort(arr)
print("Sorteeritud loend on:", arr)