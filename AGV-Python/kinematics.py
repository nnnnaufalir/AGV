import math as m
import matplotlib.pyplot as plt
import time as t

"""
konfigurasi mecanum wheel robot
 ////    \\\\
////      \\\\
    |([])|
    |([])|
\\\\      ////
 \\\\    ////
"""


#menghitung config motor berdasarkan parameter kartesian
def motorCa(args, x, y):
    return round(m.cos(m.radians(args))*x + m.sin(m.radians(args))*-y)

#menghitung config motor berdasarkan parameten silindris
def motorCy(args, pwm):
    return round(m.sin(m.radians(args))*pwm)

#menghitung resultan motor sistem silindris
def resultantCy(m1, m2, m3, m4):
    y = round(m1*m.cos(m.radians(45))+m2*m.cos(m.radians(135))+m3*m.cos(m.radians(225))+m4*m.cos(m.radians(315)))
    x = round(m1*m.sin(m.radians(45))+m2*m.sin(m.radians(135))+m3*m.sin(m.radians(225))+m4*m.sin(m.radians(315)))
    xy = round(m.sqrt(x**2+y**2))

    print(f"Fx = {x}, Fy = {y}, F.total ={xy}")
    return xy

#menghitung resultan motor sistem kartesian
def resultantCa(m1, m2, m3, m4):
    x = round(m1*m.cos(m.radians(45))+m2*m.cos(m.radians(135))+m3*m.cos(m.radians(225))+m4*m.cos(m.radians(315)))
    y = round(m1*m.sin(m.radians(45))+m2*m.sin(m.radians(135))+m3*m.sin(m.radians(225))+m4*m.sin(m.radians(315)))
    xy = round(m.sqrt(x**2+y**2))

    print(f"resultan x = {x}, y = {y}, xy ={xy}")
    return xy

# membandingkan konfigurasi kinematik sistem kartesian dan sistem silindris
# berdasarkan grafik dapat disimpulkan resultan sistem silindris sama ke segala arah
# resultan total pada sistem kartesian mencapai nilai maksimal saat 45 derajat terhadap x-axis
# dan mencapai nilai minimal saat sejajar dengan x-axis atau y-axis
# model resultan sistem kartesian berbentuk kotak sedangkan sistem silindris berbentuk lingkaran
graphXCY = []
graphYCY = []
graphXCA = []
graphYCA = []

def graphResultant(amp, ca):
    for x in range (360):
        alpha1 = 45 + x
        alpha2 = 135 + x
        alpha3 = 225 + x
        alpha4 = 315 + x

        m1 = motorCy(alpha1, amp)
        m2 = motorCy(alpha2, amp)
        m3 = motorCy(alpha3, amp)
        m4 = motorCy(alpha4, amp)

        rcy = resultantCy(m1, m2, m3, m4)

        graphXCY.append(x)
        graphYCY.append(rcy)

    for i in range (ca):
        x = ca

        alpha1 = 315 
        alpha2 = 45 
        alpha3 = 135 
        alpha4 = 225  

        m1 = motorCa(alpha1, x, i)
        m2 = motorCa(alpha2, x, i)
        m3 = motorCa(alpha3, x, i)
        m4 = motorCa(alpha4, x, i)

        rca = resultantCa(m1, m2, m3, m4)

        graphXCA.append(i)
        graphYCA.append(rca)
    
    fig, axs = plt.subplots(2)
    fig.suptitle(f'kinematicsCartesian y = {ca}')
    axs[0].plot(graphXCA, graphYCA)
    axs[0].set(ylabel='resultan', xlabel=f"x")
    axs[1].plot(graphXCY, graphYCY)
    axs[1].set(title=' kinematicsCylindrical', ylabel='resultan', xlabel='theta')
    fig.tight_layout()
    plt.subplots_adjust(wspace=2)

    plt.show()

#fungsi kinematik kartesian, mengeluarkan nilai config motor dan resultan kartesian
def kinematicsCartesian(x, y):
    alpha1 = 315 
    alpha2 = 45 
    alpha3 = 135 
    alpha4 = 225  

    m1 = motorCa(alpha1, x, y)
    m2 = motorCa(alpha2, x, y)
    m3 = motorCa(alpha3, x, y)
    m4 = motorCa(alpha4, x, y)

    print("kinematicsCartesian")
    print(f"m1 = {m1}, m2 = {m2}, m3 = {m3}, m4 = {m4}")
    print(f"x = {x}, y = {y}")
    resultantCa(m1, m2, m3, m4)

#perhitungan config motor sistem silindris
def cylindrical(theta,pwm):
    alpha1 = 45 + theta
    alpha2 = 135 + theta
    alpha3 = 225 + theta
    alpha4 = 315 + theta

    m1 = motorCy(alpha1, pwm)
    m2 = motorCy(alpha2, pwm)
    m3 = motorCy(alpha3, pwm)
    m4 = motorCy(alpha4, pwm)
    return m1,m2,m3,m4

#fungsi kinematik silindris, mengeluarkan nilai config motor dan resultan kartesian
def kinematicsCylindrical(theta, pwm):
    cylindrical(theta,pwm)
    m1, m2, m3, m4 = cylindrical(theta,pwm)[0], cylindrical(theta,pwm)[1], cylindrical(theta,pwm)[2], cylindrical(theta,pwm)[3]
    print("kinematicsCylindrical")
    print(f"m1 = {m1}, m2 = {m2}, m3 = {m3}, m4 = {m4}")
    print(f"theta = {theta}, pwm = {pwm}")
    resultantCy(m1, m2, m3, m4)

#melihat arah theta frame robot
def graphTranslation(theta):
    x = []
    for i in range(10):
        x.append(m.cos(m.radians(theta))*i)

    y = []
    for i in range(10):
        y.append(m.sin(m.radians(theta))*i)
    
    plt.plot(x, y)
    plt.grid()
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Direction ' + "\u03B8 = " + f"{theta}"+"\u00B0")
    plt.show()

#menghitung fenomena perpindahan robot dengan representasi kartesian dengan sistem silindris dalam kinematika robot
def calculateTranslationCartesian(array):
    translationX = []
    translationY = []
    distance = 0

    for path in array:
        translationX.append(path[0])
        translationY.append(path[1])

    for i in range(len(translationX)-1):
        distance += abs(translationX[i+1]-translationX[i])+abs(translationY[i+1]-translationY[i])

    endX = translationX[len(translationX)-1]
    endY = translationY[len(translationY)-1]
    begX = translationX[0]
    begY = translationY[0]
    displacement = m.sqrt((endX-begX)**2+(endY-begY)**2)
    plt.plot(translationX, translationY)
    plt.grid()
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title(f'Path distance={round(distance)}, Path displacement={round(displacement)}')
    plt.show()


# robot berotasi relatif terhadap ruang dan berpindah relatif terhadap ruang
# berotasi satu putaran namun tetap membentuk arah resultan yang sama
# gap->perubahan thetaFrame
# theta(dimulai dari x, ccw)->arah perpindahan yang diinginkan, thetaFrame(dimulai dari y, cw)->arah robot terhadap ruang
def rotatingTranslationLoop(thetaFrame, gap, delay, pwm, theta):
    total = round(360/gap)
    for i in range(total):
        t.sleep(delay)
        final = theta - thetaFrame + gap*(i)
        print(f"motor = {cylindrical(final, pwm)}, thetaFrame = {final}")

# menentukan config motor agar kinematik sesuai dengan theta
# biarpun nilai thetaFrame acak
def rotatingTranslationTheta(thetaFrame, theta, pwm):
    final=theta-thetaFrame
    print(cylindrical(final, pwm))
    print(final)

# calculateTranslationCartesian([[0,0],[100,100], [200,100], [100,200], [0,0]])
# rotatingTranslationTheta(90, 90, 100)
# rotatingTranslationLoop(90, 45, 0.1, 100, 90)