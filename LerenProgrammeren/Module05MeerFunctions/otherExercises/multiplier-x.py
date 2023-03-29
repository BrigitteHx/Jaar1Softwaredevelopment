#multiplier-x.py

def multiplier(tafel):
    result = ""
    for i in range(1,11):
        result += f"{i} x {tafel} = {i*tafel}\n"
    return result

print(multiplier(tafel = int(input("Kies een tafel van 1-10. "))))
