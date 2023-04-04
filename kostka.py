#!/usr/bin/env python3

import random

class Kostka:
  """
  Trida reprezentujici hraci kostku.
  """

  def __init__(self, pocetSten=6):
    if (pocetSten > 1):
      self.__pocetSten = pocetSten
    else:
      print("Kostka musi mit 2 a vice sten.")

  def hod(self):
    return random.randint(1, self.__pocetSten)

  def __str__(self):
    return f"Kostka s {self.__pocetSten} stenami."
  
  def getPocetSten(self):
    return self.__pocetSten
  
def main():
  k = Kostka(12)
  print(k)
  print(k.getPocetSten())
  print(k)



if __name__=="__main__":
  main()

