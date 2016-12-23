# Simulasi Persamaan gerak Osilasi
from math import pow


import matplotlib.pyplot as plt
from decimal import *

"""
def equationOfOsi():
    k = 1.0
    m = 1.0
    t0 = 0.0
    h = 0.1
    n = 500
    # syarat awal x(t) dab v(t)
    x0 = 0.0
    #v0 = 0.3367
    v0 = 2.0
    ###fungsi F ruas kanan dari persamaan differensial###
    fv = -k * x0 / m
    fx = v0

    ## Metode Euler dengan menghitung v(t) dan x(t)
    ## disertai menghitung tenaga total pada setiap waktu
    ##looping

    print("||iterasi ke || waktu ke \t || posisi X \t || Kecepatan \t || Tenaga")
    for i in range(0,n+1):
        time,pos,velo,tenagaArr=[],[],[],[]
        ti = i * h
        #vi = v0 + h * fv
        vi = v0 + h * fv
        xi = (x0 + (h * fx))

        tenaga =  ((m * vi**2) / 2.0) + ((k * xi**2) / 2.0)
        print("||" ,i ,"\t\t || %.5f" % ti ,"\t || %.5f" % xi,"\t || %.5f" % vi,"\t || %.5f" % tenaga)
        v0 =  vi
        x0 = xi
        fv = -k * x0 / m
        fx = v0

    #Drawing plot
        time.append(ti)
        pos.append(xi)
        velo.append(vi)
        tenagaArr.append(tenaga)
        plt.title('Gelombang Osi')
        plt.xlabel('time (s)')
        plt.ylabel('nganu')
        plt.plot(time, pos,'go')
        plt.plot(time, velo, 'bo')
        plt.plot(time, tenagaArr, 'ro')
        plt.grid(True)


    plt.show()



equationOfOsi()
#tenaga =  ((1.0 * 2**2) / 2.0) + ((1.0 * 0.2**2) / 2.0)
#print(tenaga)

"""
def coba():
    asu='nganu'
    hasil=1+1
    hasil1=0.5**3

    print("",hasil1 , " ",hasil)

coba()


#print("hello world ini main fungsi")