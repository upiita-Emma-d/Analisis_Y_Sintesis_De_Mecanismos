def pro(E,l,r):
    import sys, math
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    e=E
    L=l
    R=r
    w=((30*2*math.pi)/60)
    #print(w)
    Bp=math.asin(e/(L+R))
    #print(math.degrees(Bp))
    Bpp=math.asin(e/(L-R))
    #print(math.degrees(Bpp))
    fi=Bpp-Bp
    Xcp=math.sqrt(math.pow((L+R),2) - math.pow(e,2))
    #print(Xcp)
    Xcpp=(L-R)*math.cos(Bpp)
    #print(Xcpp)
    Ycp=(L+R) * (math.pow(math.sin(Bp),2))
    Ycpp=(L-R) * math.pow(math.sin(Bpp),2)
    #print(Ycp)
    #print(Ycpp)
    Rt=(math.pi + fi)/(math.pi-fi)
    #print(Rt)
    Tciclo=(2*math.pi)/w
    t1=(Tciclo)/(Rt+1)
    #print(t1)
    t2=(Tciclo-t1)
    #print(t2)
    #print(t1+t2, Tciclo)
    Xcv.append(e/(math.tan((Bpv*2*math.pi)/360)));
    Ycv.append((L+R)*(math.sin((Bpv*2*math.pi)/360)**2));

    # Data for plotting
    fig, ax = plt.subplots()
    print(Xcv)
    ax.plot(Xcv, Ycv)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    fig.savefig("test.png")
    plt.show()

def main():
    #E = float(input("Dame la exentricidad:"))
    #l = float(input("Dame la logitud mayor:"))
    #r = float(input("El radio"))
    E=.3
    l=.7
    r=.3
    pro(E,l,r)




if __name__ == '__main__':
    main()
