#fibonacci

# research: 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# de eerste 2 termen zijn 0 en 1, de derde term is de 2 hiervoor opgeteld -> zo door
# som = nummer_nu = nummer_1 + nummer_2                                                    

# kort handmatig ----------------------------------------------------------------------------------------------------------------------

# def fibonacci():
#     nummer_begin = int(input("Hoeveel keer wilt u de fibonacci toepassen? "))   #1    
#     nummer1, nummer2 = 0, 1                                                          # dit zijn de eerste 2 nummers (om te beginnen bij 0 en 1)
#     score = 0                                                                        # score voor loop en optellen 
#     print(f"Dit is de fibonacci na {nummer_begin} keer:") #2
#     while(score<nummer_begin):                                                     
#         print(nummer1)
#         som = nummer1 + nummer2        #3                                        # som, zie research
#         nummer1 = nummer2                                                        # nieuw nummer 1
#         nummer2 = som                                                            # nieuw nummer 2
#         score += 1                                                            

# fibonacci()

# # kort met list  ----------------------------------------------------------------------------------------------------------------------

# fibonacci_lijst = [0, 1]
# nummer_invoer = int(input("Hoeveel keer wilt u de fibonacci toepassen? "))

# for stap in range(3, nummer_invoer + 1):
#     waarde = fibonacci_lijst[stap - 2] + fibonacci_lijst[stap - 3]
#     fibonacci_lijst.append(waarde)
# print(fibonacci_lijst)

# poging 3 ----------------------------------------------------------------------------------------------------------------------

# nummer_invoer = int( input("Hoeveel keer wilt u de fibonacci toepassen? "))

# def fibonacci(nummer_invoer):
#     nummer1 = 0
#     nummer2 = 1
#     fibonacci_lijst = [0, 1]
#     for i in range(nummer_invoer - 2):
#         nieuw_nummer = nummer1 + nummer2
#         nummer1 = nummer2
#         nummer2 = nieuw_nummer
#         fibonacci_lijst.append(nieuw_nummer)
#     return fibonacci_lijst

# print(fibonacci(nummer_invoer))

# uiteindelijk ----------------------------------------------------------------------------------------------------------------------

nummer = int( input("Hoeveel keer wilt u de fibonacci toepassen? ")) 

def fibonacci(nummer):
    if nummer <=1:
        return nummer
    else:
        return (fibonacci(nummer-1) + fibonacci(nummer-2)) # som 
            #   som = n1 + n2  
            #   n1 = n2
            #   n2 = som
            #   i += 1

if nummer <= 0:
  print("Alleen maar getallen in de +")

for i in range(nummer):  
      print(fibonacci(i))
