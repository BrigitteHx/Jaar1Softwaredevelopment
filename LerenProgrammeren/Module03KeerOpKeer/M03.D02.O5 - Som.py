#M03.D02.O5 - Som > 1000


for verandering in range (2,50):
    verandering = 1

i = 50
som = i + verandering

while i <= 999:
    if i == 1000:
        break
    print(i)
    i = som + i + verandering # nieuwe waarde voor I maken!
print("einde")
