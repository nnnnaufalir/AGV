import pathPlanningFunc as pp
import numpy as np
import math as m
from itertools import count
import time
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

A = ["A", {"B" : [100,0], "Z" : [200,180]}]
B = ["B", {"V" : [150,0], "A" : [100,180]}]
V = ["V", {"B" : [150,180], "C" : [200, 90]}]
C = ["C", {"V" : [200,270], "D" : [500,90]}]
D = ["D", {"E" : [100, 90], "C" : [500,270]}]
E = ["E", {"D" : [100, 270], "G" : [500,180]}]
Z = ["Z", {"A" : [100, 0], "I" : [500,90]}]
G = ["G", {"E" : [100,0], "I" : [100,90]}]
I = ["I", {"G": [100,0], "Z" : [100,270]}]
stateX = 0
stateY = 0

def move(path):

    cartesianPath = []
    for i in range(len(path)-1): 
        a = localVar[path[i]][1][path[i+1]]
        x = round(a[0] * m.sin(a[1]/57.2958))
        y =  round(a[0] * m.cos(a[1]/57.2958))
        cartesianPath.append([x,y])


    ordoX = []
    ordoY = []

    print(cartesianPath) 
    def member(a,ordo, num):
        global stateX, stateY
        if num == 0:
            for j in np.linspace(stateX, a[num]+stateX, 100):
                ordo.append(j)
            stateX += a[num]
            print(stateX)
        if num == 1:
            for j in np.linspace(stateY, a[num]+stateY, 100):
                ordo.append(j)
            stateY += a[num]
            print(stateX)

    for i in cartesianPath:
        member(i, ordoX, 0)
        member(i, ordoY, 1)

    def simulation():
        # fungsi animasi
        index = count()
        x = []
        y = []
        def animate(i):
            try:
                x.append(ordoX[next(index)])
                y.append(ordoY[next(index)])
            except IndexError:
                print("masih ada bug:)")
            plt.cla()
            plt.ylim(-max(ordoY)*1.1, max(ordoY)*1.1)
            plt.xlim(-max(ordoX)*1.1, max(ordoX)*1.1)
            # menggambar garis pada figure
            plt.plot(x, y)
            # menjalankan fungsi agar figure terlihat semua (responsif)
            plt.tight_layout()
        # memanggil fungsi dasar untuk plotting realtime
        ani = FuncAnimation(plt.gcf(), animate, interval = 1)
        # menampilkan figure
        plt.tight_layout()
        plt.show()

    simulation()

localVar = locals()