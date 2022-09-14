from sys import path
from PathPlanning import PathPlanning
from MoveCalculation import MoveCalculation
from MoveSimulation import Simulation
import serial
import time

class Toolbox(PathPlanning, MoveCalculation, Simulation):
    pass

a = Toolbox()
a.setState("A")
# a.simulation(a.pathPlanningStep("D"))
run = a.pathPlanningStep("D", status=False)
counterA = 0
#print(run)

def rencana () :
    for i in range(len(run)):
        if i<1:
            path = str((run[counterA][0]))
            jarak = str((run[counterA][1]))
            derajat = str((run[counterA][2]))
            tujuan = str((run[counterA][3]))
    
    total = path + ',' + jarak + ',' + derajat + ',' + tujuan + '$'
    return total

# #cam = 'krai' + '#' + ','
if __name__ == '__main__':
    ser = serial.Serial('COM13',115200, timeout=1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            if counterA > len(run) : 
                counterA=0
            if line == "Path Selesai":
                counterA +=1
            ser.write(b"" + rencana().encode())
            print(rencana())
            print(line)
   
