from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.speed = 2
teller = 1 
while teller > 0 and teller < 10: # van de or een and maken
    robotArm.grab()
    color = robotArm.scan()
    # if color == "red" or "green" or "yellow" or "blue" or "white":        -> niet nodig ivm regel 17 
    for i in range (teller):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(teller):
        robotArm.moveLeft()
    teller = teller + 1
    if color == '':              # -> niet nodig ivm and 
        teller = 10              # zelfde effect als break want teller = false 
robotArm.wait()