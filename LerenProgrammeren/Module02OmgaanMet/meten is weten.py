# meten is weten

a = int(input("Waarde A: ")) 
b = int(input("Waarde B: "))

if a > b: 
    min = b 
    max = a 
    print("Het minimum is", min)
    print("Het maximum is", max)
elif a < b:
    min = a 
    max = b 
    print("Het minimum is", min)
    print("Het maximum is", max)
else: a==b, print("A en B zijn gelijk")
    
