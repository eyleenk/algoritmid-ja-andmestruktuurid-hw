class Järjekord:
    def __init__(self):
        self.elemendid = [] # Loob tühja nimekirja, mis on järjekorra aluseks

    def on_tühi(self): 
        return len(self.elemendid) == 0 #Kontrollib, kas järjekord on tühi 

    def lisa(self, element):
        self.elemendid.append(element)  #Lisab elemendi järjekorra lõppu

    def eemalda(self):
        if self.on_tühi():
            raise IndexError("Eemalda tühjast järjekorrast") #Kui järjekord tühi, siis error
        return self.elemendid.pop(0) #Eemaldab ja tagastab esimese elemendi järjekorrast

    def esimene(self):
        if self.on_tühi():
            raise IndexError("Esimene tühjast järjekorrast")
        return self.elemendid[0] #Tagastab esimese elemendi järjekorrast ilma eemaldamata

    def suurus(self):
        return len(self.elemendid) #Tagastab elemendite arvu
    
if __name__ == "__main__": #Koodi testimine
    järjekord = Järjekord()
    järjekord.lisa(1)
    järjekord.lisa(2)
    järjekord.lisa(3)
    print("Järjekorra suurus:", järjekord.suurus())
    print("Esimene element:", järjekord.esimene()) 
    print("Eemaldatud element:", järjekord.eemalda())
    print("Järjekorra suurus pärast eemaldamist:", järjekord.suurus())
    print("Kas järjekord on tühi?", järjekord.on_tühi())