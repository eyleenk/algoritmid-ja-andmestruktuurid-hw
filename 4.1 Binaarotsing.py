def binaarotsing (arr, a):
    if not isinstance(a, int):
        return ("Element peab olema täisarv")
    vasak, parem = 0, len(arr)-1
    while vasak <= parem:
        keskm = (vasak + parem) // 2
        if arr[keskm] == a:
            return keskm
        elif arr[keskm] < a:
            vasak = keskm + 1
        else:
            parem = keskm - 1
    return ("Element ei ole listis")
    
#test
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a= 3,5
print(binaarotsing(arr, a))