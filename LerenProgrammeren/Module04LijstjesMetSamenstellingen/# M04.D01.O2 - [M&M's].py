# M04.D01.O2 - [M&M's]
import random

kleurMM = ('oranje ', 'blauw ', 'groen ', 'bruin ')
MMzak = 0

while True: 
    print(f"Er zitten {MMzak} M&M's in de M&M zak. ")
    hoeveelheidMM = int(input("Hoeveel M&M's wilt u in de zak doen? "))
    MMzak = hoeveelheidMM

    if hoeveelheidMM > 0:
        for i in range(hoeveelheidMM):
            print(random.choice(kleurMM))
    else: 
        print("Vul aub een correct antwoord in")
    print(f"Er zitten nu {MMzak} M&M's in de M&M zak. ")
    break 


