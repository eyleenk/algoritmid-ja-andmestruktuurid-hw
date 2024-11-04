def selection_sort(arr):  #defineerib funktsiooni, mis kasutab Selection Sort algoritmi
    for i in range(len(arr)):  #läbib listi liikmed ja seab i väärtuseks hetkeindeksi
        min_index = i  #määrab muutuja, mis näitab hetkel väikseimat elementi sorteerimata osas
        for j in range(i + 1, len(arr)):  #läbib ülejäänud listi liikmed, et leida väikseim element
            if arr[j] < arr[min_index]:  #kui leitakse väiksem element, uuendatakse min_index väärtust
                min_index = j  #määrab min_index väärtuseks j, kui leitakse väiksem element
        arr[i], arr[min_index] = arr[min_index], arr[i]  #vahetab hetkepositsioonil oleva elemendi väikseima elemendiga

# Test
arr = [29, 15, 56, 77, 18] 
selection_sort(arr)  
print(arr)  