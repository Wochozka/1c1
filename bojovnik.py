#!/usr/bin/env python3

import kostka

class Bojovnik:
    """
    Trida reprezentujici bojovnika
    """

    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        self.__jmeno = jmeno
        self.__zivot = zivot
        self.__maxZivot = zivot
        self.__utok = utok
        self.__obrana = obrana
        self.__kostka = kostka
        self._zprava = ""

    def __str__(self):
        return f"Bojovnik jmenem {self.__jmeno}."
    
    def utok(self, souper):
        uder = self.__utok + self.__kostka.hod()
        souper.obrana(uder)
    
    def obrana(self, uder):
        obrana = self.__obrana + self.__kostka.hod()
        zraneni = uder - obrana
        zprava = f"{self.__jmeno} utrpel zraneni o sile {zraneni}."
        if zraneni < 0:
            zraneni = 0
            zprava = f"{self.__jmeno} zcela odrazil utok."
        self.__zivot = self.__zivot - zraneni
        if self.__zivot <= 0:
            self.__zivot = 0
            zprava = zprava[:-1] + " a zemrel."
        self.setZprava(zprava)


    
    def grafickyZivot(self):
        celkem = 20
        pocet = int(self.__zivot / self.__maxZivot * celkem)
        return f"[{'#'*pocet}{' '*(celkem-pocet)}]"
    
    @property
    def nazivu(self):
        return self.__zivot > 0
    
    def setZprava(self, zprava):
        self._zprava = zprava
    
    def getZprava(self):
        return self._zprava


def main():
    k = kostka.Kostka(10)
    denisa = Bojovnik("Denisa", 100, 40, 30, k)
    prvnic = Bojovnik("1c", 120, 50, 35, k)
    
    denisa.utok(prvnic)
    print(prvnic, prvnic.grafickyZivot())

    prvnic.utok(denisa)
    print(denisa, denisa.grafickyZivot())

    denisa.utok(prvnic)
    print(prvnic, prvnic.grafickyZivot())

if __name__ == "__main__":
  main()

