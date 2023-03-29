from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:

teller = 9
while teller < 10 and teller > 0 :
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for i in range(0,teller): 
            robotArm.moveRight()
        robotArm.drop()
        teller = teller - 1 
        for i in range(0,teller):
            robotArm.moveLeft()
    elif color == "white" or "blue" or "yellow" or "green" or "" :
        robotArm.drop()
        robotArm.moveRight()
        teller = teller - 1
robotArm.wait()
