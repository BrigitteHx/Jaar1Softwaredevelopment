# fibonacci 2

nummer = int( input("Hoeveel keer wilt u de fibonacci toepassen? ")) 

# een recursieve function is een functie die zichzelf kan oproepen en herhalen zoals een loop 

def fibonacci2(nummer):
    print(f"fibonacci aangeroepen met {nummer}")
    if nummer <= 1:
       return nummer
    else:
       return(fibonacci2(nummer-1) + fibonacci2(nummer-2))

# checken of de invoer boven de 0 is 

if nummer <= 0:
   print("Alleen maar getallen in de +")
else:
   for i in range(nummer):
       print(fibonacci2(i))

print(fibonacci2(3))