# Simulasi Persamaan gerak Osilasi
from math import pow
import matplotlib.pyplot as plt

def drawPlot(waktu,posisi,kecepatan,pwr,n):
    print("processing plot, please wait !")
    while n!=0:
        plt.plot(waktu, posisi, '-g')
        plt.plot(waktu,kecepatan, '--b')
        plt.plot(waktu, pwr, '-r')
        n=n-1

    """ Start Drawing plot"""
    plt.title('Gelombang Osi')
    plt.xlabel('time (s)')
    plt.ylabel('nganu')
    plt.grid(True)
    plt.show()
    # End Drawing plot

def equationOfOsi():
    k = 1.0
    m = 1.0
    deltaT = 0.1
    n = int(5/deltaT)
    # syarat awal x(t) dab v(t)
    x0 = 0.0
    v0 = 2
    #v0 = 1.0

    ## Metode Euler dengan menghitung v(t), x(t) dan E total pada setiap waktu
    time, pos, velo, tenagaArr = [], [], [], []

    print("||iterasi ke || waktu ke \t || posisi X \t || Kecepatan \t || Tenaga")

    """ Start For """
    for i in range(0,n+1):
        ti = i * deltaT
        vi = v0 + deltaT * (-k * x0 / m)
        xi = x0 + (deltaT * v0)
        tenaga = m * pow(vi,2)/ 2.0 + k *pow(xi,2) / 2.0
        print("||", i, "\t\t || %.5f" % ti, "\t || %.5f" % xi, "\t || %.5f" % vi, "\t || ",tenaga)
        #print("|| ", i, "\t\t || " , ti, "\t || " , xi, "\t || " , vi, "\t || ", tenaga)
        v0 = vi
        x0 = xi
        time.append(ti)
        pos.append(xi)
        velo.append(vi)
        tenagaArr.append(tenaga)
    """ End For """
    drawPlot(time, pos, velo, tenagaArr, n)

"""Run Program"""
equationOfOsi()
# tenaga =  ((1.0 * 2**2) / 2.0) + ((1.0 * 0.2**2) / 2.0)
# print(tenaga)
