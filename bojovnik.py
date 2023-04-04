#!/usr/bin/env python3

import kostka

class Bojovnik:
    """
    Trida reprezentujici bojovnika
    """

    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        self.__jmeno = jmeno
        self.__zivot = zivot
        self.__utok = utok
        self.__obrana = obrana
        self.__kostka = kostka

    def __str__(self):
        return f"Bojovnik jmenem {self.__jmeno}."

def main():
    k = kostka.Kostka(10)
    b = Bojovnik("Denisa", 100, 40, 30, k)
    print(b)

if __name__ == "__main__":
  main()

