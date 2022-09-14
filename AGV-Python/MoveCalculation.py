import math as m

class MoveCalculation:
    def __init__(self):
        self.leftWheelPulse = 0
        self.rightWheelPulse = 0
        """A class to defining specification of diferential drive robot

        ...

        Parameters
        ----------
        leftWheel : float
            Diameter at left wheel
 
        leftWheel : float
            Diameter at right wheel

        diameterRobot : float
            Diameter of differential drive system, distance from right wheel to left wheel 
        """
        pass
    def setSpecs(self, leftWheel, rightWheel, diameterRobot, wheelPulse):
        self.leftWheel = leftWheel
        self.rightWheel = rightWheel
        self.diameterRobot = diameterRobot
        self.wheelPulse = wheelPulse
        print("done")

    def run(self, pulse):
        self.leftWheelPulse += pulse
        self.rightWheelPulse += pulse
    def rotate(self, degree):
        if degree<= 180 and degree>0:
            self.leftWheelPulse += degree * (self.leftWheel/self.diameterRobot) / 180 * self.wheelPulse
            self.rightWheelPulse -= degree * (self.rightWheel/self.diameterRobot) / 180 * self.wheelPulse
            return self.leftWheelPulse, self.rightWheelPulse
        if degree >180 and degree <=360:
            self.leftWheelPulse -= degree * (self.leftWheel/self.diameterRobot) / 180 * self.wheelPulse
            self.rightWheelPulse += degree * (self.rightWheel/self.diameterRobot) / 180 * self.wheelPulse
            return self.leftWheelPulse, self.rightWheelPulse
    def rotationOdometryWheel(self, leftRotationPulse, rightRotationPulse):
        """Return an value that figure out rotation degree

        Calculating rotation degree using infomation of left wheel rotation and right wheel rotation

        Parameters
        ----------
        leftRotation : float
            How much rotation at left wheel

        rightRotation : float
            How much rotation at right wheel

        Return
        ------
            Rotation degree
        """
        result = (self.leftWheel*leftRotationPulse-self.rightWheel*rightRotationPulse)/(2*self.diameterRobot) * 180 / self.wheelPulse
        while True:
            if result>=360: result -= 360
            elif result<=-360: result += 360
            else: break
        return result
                
    def backToTrajectory(self, wallDistance, deg):
        """Return an value that figure out distance while turning after avoiding

        While doing an movement, robot can have an obstacle in their trajectory or planning
        therefore, robot calculating how far they must to go for avoiding the obstacle
        since robot also using wall following, distance information from ultrasonic sensor will be used

        Parameters
        ----------
        wallDistance : int 
            Distance from robot to wall

        degree : int
            Degree for direction

        Return
        ------
            Distance for movement robot
        """
        return wallDistance/m.cos(deg/57.2958)
    def avoidObstacle(self, forward, degree, valueY = False):
        """Return an value that figure out distance while turning for avoiding

        While doing an movement, robot can have an obstacle in their trajectory or planning
        therefore, robot calculating how far they must to go after avoiding the obstacle
        since robot also using wall following, distance information from ultrasonic sensor will be used

        Parameters
        ----------
        forward : integer 
            Distance forward movement

        degree : integer
            Degree for direction

        valueY : boolean, optional
            If false return X value else Y value (default false)

        Return
        ------
            Distance for movement robot
        """
        resultX = abs(forward/m.cos(degree/57.2958))
        resultY = abs(m.tan(degree*57.2958) * forward)
        return resultX if (valueY == False) else resultY

a = MoveCalculation()
a.setSpecs(10.0,10.0,10, 40)
print(a.rotationOdometryWheel(40,-40))
print(a.rotate(180))