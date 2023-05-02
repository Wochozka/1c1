#!/usr/bin/env python3

import kostka
import bojovnik

class Arena():

    def __init__(self, bojovnik1, bojovnik2, kostka):
        self.bojovnik1 = bojovnik1
        self.bojovnik2 = bojovnik2
        self.kostka = kostka
    
    def vykresli(self):
        self.vycisti()
        print("----------- Arena ------------\n")
        print("Bojovnici:")
        self.vykresliBojovnika(self.bojovnik1)
        self.vykresliBojovnika(self.bojovnik2)

    def vycisti(self):
        import subprocess
        subprocess.call("clear")
    
    def vypisZpravu(self, zprava):
        import time
        print(zprava)
        time.sleep(1)

    def vykresliBojovnika(self, bojovnik):
        print(bojovnik)
        print("Zivot:", bojovnik.grafickyZivot())

    def zapas(self):
        self.vykresli()

        print("Vitejte v arene.")
        print(f"Dnes se utkaji {self.bojovnik1} a {self.bojovnik2}.")

        while self.bojovnik1.nazivu and self.bojovnik2.nazivu:
            self.bojovnik1.utok(self.bojovnik2)
            self.vykresli()
            self.vypisZpravu(self.bojovnik1.getZprava())
            self.vypisZpravu(self.bojovnik2.getZprava())

            if self.bojovnik2.nazivu:
                self.bojovnik2.utok(self.bojovnik1)
                self.vykresli()
                self.vypisZpravu(self.bojovnik2.getZprava())
                self.vypisZpravu(self.bojovnik1.getZprava())


if __name__ == "__main__":
    k = kostka.Kostka(20)
    erik = bojovnik.Bojovnik("Erik", 100, 80, 50, k)
    richard = bojovnik.Bojovnik("Richard", 110, 60, 50, k)

    a = Arena(erik, richard, k)
    a.zapas()
