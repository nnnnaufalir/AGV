import math as m
def rotationOdometry(l, r, a):
    return (l-r)/a * 180

def turnAvoidingHuman(l, deg):
    return l/m.cos(deg / 57.2958)

print(rotationOdometry(20, 10, 100))

print(turnAvoidingHuman(5, 45))