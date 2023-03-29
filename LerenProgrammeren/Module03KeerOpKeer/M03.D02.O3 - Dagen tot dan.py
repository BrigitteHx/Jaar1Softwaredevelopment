#M03.D02.O3 - Dagen tot dan

dagen = [ "ma", "di", "wo", "do", "vr", "za", "zo" ]

while True:
    welkedag = input("Welke dag is het vandaag? Kies uit ma, di, wo, do, vr, za, zo. ")
    if welkedag in dagen:
        break 

num = 0

restdagen = True 
while restdagen: 
    print(dagen [num])
    if welkedag == dagen [num]:
        break 
    num = num + 1
print(f'nog {num + 1} dagen')
