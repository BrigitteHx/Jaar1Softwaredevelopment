#M03.D02.O1 - Blastoff
import time

aftellen = int(input("Vanaf hoeveel seconden wilt u aftellen? "))

while aftellen < 31:
    print(f'nog {aftellen} seconden')
    aftellen = aftellen -1
    time.sleep(1)
    if aftellen == 0:
        break 
