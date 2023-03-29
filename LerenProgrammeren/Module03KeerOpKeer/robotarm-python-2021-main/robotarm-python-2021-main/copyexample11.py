from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

for i in range(10):
   robotArm.moveRight()

for i in range(11):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()
