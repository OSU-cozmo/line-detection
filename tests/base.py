import lineDetection
import CozmOSU


robot = CozmOSU.Robot()

def main(robot : CozmOSU.Robot):
    robot.say("Hello")



robot.start(main)