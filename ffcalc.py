#!/usr/bin/python3

import matplotlib.pyplot as p

g = 9.81
cw = 0.45
A = 1
rho_l = 1.29
m = 1
k = 0.29025 # A * rho_l * cw
delta_t = 0.1
v_0 = 0
y_0 = 0

def t_neu(t_alt):
    return t_alt + delta_t

def a_neu(v_alt):
    return -g + k/m * v_alt*v_alt

def v_neu_full(v_alt):
    return v_alt + a_neu(v_alt) * delta_t

def v_neu_1():
    return v_0 + a_neu(v_0) * delta_t/2

def v_neu(v_alt):
    return v_alt + a_neu(v_alt) * delta_t

def y_neu_1():
    return y_0 + v_neu_1() * delta_t

def y_neu(y_alt, v_alt):
    return y_alt + v_neu(v_alt) * delta_t

def main():
    v = v_neu_1()
    a = a_neu(v_0)
    y = y_neu_1()
    t = t_neu(0)
    vl = []
    al = []
    yl = []
    tl = []
    while True:
        # add list items
        vl.append(v)
        al.append(a)
        yl.append(y)
        tl.append(t)
        if(v_neu(v) == v):
            break
        y = y_neu(y, v)
        v = v_neu(v)
        a = a_neu(v)
        t = t_neu(t)
    p.plot(tl, vl)
    p.xlabel('t')
    p.ylabel('v')
    p.show()
    p.plot(tl, al)
    p.xlabel('t')
    p.ylabel('a')
    p.show()
    p.plot(tl, yl)
    p.xlabel('t')
    p.ylabel('y')
    p.show()

if __name__ == "__main__":
    main()
