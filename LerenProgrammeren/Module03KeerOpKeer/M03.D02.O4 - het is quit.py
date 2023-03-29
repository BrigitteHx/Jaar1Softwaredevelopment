#M03.D02.O4 - het is quit

antwoord = [ "quit", "Quit" ]
num = 1 

while True:
    vraag = input("wat is het wachtwoord? ")
    if vraag in antwoord:
        break 
    if not vraag in antwoord: 
        num = num + 1
print(f'{num} pogingen.')
