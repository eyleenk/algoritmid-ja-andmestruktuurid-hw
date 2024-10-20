def fibonacci (n): 
    if n % 1 != 0:
        print("Viga! Arv peab olema täisarv!")
        return
    if n < 0:
        print("Viga! Arv peab olema positiivne!")
        return
    if n<= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#test
print(fibonacci(-1))
print(fibonacci(1.5))
print(fibonacci(10))
print(fibonacci(5))

# Kutsub välja funktsiooni fibonacci, mis leiab Fibonacci jada n-nda liikme. Kui n on suurem, kui 1, siis kutsub end ise välja (e. on rekursiivne) 
# kahe erineva arvuga, esimesel juhul argumendiga n-1, ehk siis jada eelmine liige, teisel juhul argumendiga n-2, ehk siis jada liige enne eelmist liiget. 
# Kuna fibonacci jada kujutab endast jada, kus iga liige on kahe eelneva liikme summa, siis ongi vaja eelnev ja jjärgmine liige kokku liita. Fibonacci 
# esimesed liikmed on 1, 1, 2, 3, 5, 8, 13, 21, 34, 55. Kõik liikmed peavad olema täisarvud ja ilma komakohata.