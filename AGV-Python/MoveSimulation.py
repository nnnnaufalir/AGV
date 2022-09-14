from time import sleep, time
from MoveCalculation import MoveCalculation
class Simulation:
    def __init__(self) -> None:
        pass
    def simulation(self, plan):
        for i in range(len(plan)):
            print("jarak:", plan[i][1])
            print(self.rightWheelPulse)
            sleep(0.01)
            if not plan[i-1][2] == plan[i][2] and i>0:
                print(plan[i][2])
