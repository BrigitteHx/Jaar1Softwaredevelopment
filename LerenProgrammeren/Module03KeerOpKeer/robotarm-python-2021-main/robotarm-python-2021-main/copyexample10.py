from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
distance = 9 
for i in range(5):
    robotArm.grab()
    for move in range(distance):
        robotArm.moveRight()
    distance = distance - 1 
    robotArm.drop()
    for move in range(distance):
        robotArm.moveLeft()
    distance = distance -1 
robotArm.wait()