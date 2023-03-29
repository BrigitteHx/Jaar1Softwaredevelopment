from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = (2)

# Jouw python instructies zet je vanaf hier:

for i in range(7):
    robotArm.moveRight()
robotArm.grab()
    
for i in range(1):
     robotArm.moveRight()
robotArm.drop()

for i in range(7):
    for i in range(2):
        robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()