#klassen opdracht

import random

naam = input("wat is je naam? ")
hoeveel_complimenten = int(input("hoeveel complimenten wil je? "))

complimenten = ["je bent mooi", "je bent aardig", "je bent slim", "je bent geweldig", "je bent speciaal"]

complimenten_kopie = complimenten[:]                      # copy
random.shuffle (complimenten_kopie)                       # random keuze shuffelen 
for i in range(hoeveel_complimenten):       
    print(f"{complimenten_kopie.pop()} {naam}")           # niet dezelfde kiezen/ vw van lijst 
    if complimenten_kopie == []:
        complimenten_kopie = complimenten                 # nieuwe random lijst genereren 