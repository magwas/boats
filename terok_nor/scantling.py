#!/usr/bin/python
from __future__ import division
import sys
from sympy import *

#mm, m, cm = symbols('mm, m, cm')
data = {}

L, L_wl, a, b, l, v, R = symbols("L, L_wl, a, b, l, v, R")

data[L] = 7.0
data[L_wl] = 7.0
#data[a] = 385.0 #385 mm is recommended
data[v] = 25.0 #kn
data[R] = l/a
#R: width/height of unsupported plate panels

P_dbsf, P_dbsa, P_dssf, P_dssa = symbols("P_dbsf, P_dbsa, P_dssf, P_dssa")
P_dbmf, P_dbma, P_dsmf, P_dsma = symbols("P_dbmf, P_dbma, P_dsmf, P_dsma")
P_dD = symbols("P_dD ")
F_vb, F_vs, F_vf, P_dd, F_p, F_vl, F_vsf, F_vsl, F_vbw, F_vsw = symbols("F_vb, F_vs, F_vf, P_dd, F_p, F_vl, F_vsf, F_vsl, F_vbw, F_vsw")

data[P_dbsf] = 3.29*L-1.41
data[P_dbsa] = 2.63*L-1.13
data[P_dssf] = 2.06*L-2.94
data[P_dssa] = 1.65*L-2.35
data[P_dbmf] = 2.7*L+3.29
data[P_dbma] = 2.16*L+2.63
data[P_dsmf] = 1.88*L+1.76
data[P_dsma] = 1.5*L+1.41
data[P_dd] = 0.26*L+8.24

data[F_p] = (0.54*0.23*R)
data[F_vb] = 0.34*sqrt(v/sqrt(L_wl))+0.355
data[F_vs] = (0.024*sqrt(v/sqrt(L_wl))+0.91)*(1.018-0.0024*L)
data[F_vf] = (0.78*sqrt(v/sqrt(L_wl))+0.48)*(1.335-0.01*L)
data[F_vl] = 0.075*v/sqrt(L_wl)+0.73
data[F_vbw] = data[F_vl]
data[F_vsf] = (0.1*sqrt(v/sqrt(L_wl))+0.52)*(1.19-0.01*L)
data[F_vsw] = data[F_vsf]
data[F_vsl] = (0.14*sqrt(v/sqrt(L_wl))+0.47)*(1.07-0.008*L)

for f in [F_vb, F_vs, F_vf, F_vl, F_vsf, F_vsl, F_vbw, F_vsw]:
    value = data[f].subs(data)
    print f, value
    if value < 1.0:
        print f,"is less than 1:", value, ", fixed"
        data[f] = 1.0

G_WB, G_WS, G_WS_min, G_WB_min, G_WF, G_WK, G_K, G_WD, G_WD_min = symbols("G_WB, G_WS, G_WS_min, G_WB_min, G_WF, G_WK, G_K, G_WD, G_WD_min")

G, G_min, P, F_v = symbols("G, G_min, P, F_v")
data[G] = 1.57*b*F_p*F_v*sqrt(P)
data[G_min] = 1.1*(350+5*L)*sqrt(P)

w_keel, G_K = symbols("w_keel, G_K")

data[w_keel] = 25*L+300
data[G_K] = 2.35*(350+5*L)*sqrt(P_dbmf)

W_BL, W_BL_min, W_SL, W_SL_min, W_RM, W_RM_min, W_RS, W_RS_min = symbols("W_BL, W_BL_min, W_SL, W_SL_min, W_RM, W_RM_min, W_RS, W_RS_min")
e, l = symbols("e,l")
k5 = max(0.01*data[L]+0.7,0.75)
print "k5=", k5

k6 = max(0.045 * data[L] + 0.10,0.6)
print "k6=", k6

data[W_BL] = 2.14*e*l*l*F_vl*P*0.001
data[W_BL_min] = 2.14*e*k5*k5*F_vl*P*0.001
data[W_SL] = 2.07*e*l*l*F_vl*P*0.001
data[W_SL_min] = 2.07*e*k5*k5*F_vsl*P*0.001
data[W_RM] = 3.21*e*l*l*F_vbw*P*0.001
data[W_RM_min] = 3.21*e*k6*k6*F_vbw*P*0.001
data[W_RS] = 2.18*e*l*l*F_vsw*P*0.001
data[W_RS_min] = 2.18*e*k6*k6*F_vsw*P*0.001

minimums = dict()
minimums[W_BL] = W_BL_min
minimums[W_SL] = W_SL_min
minimums[W_RM] = W_RM_min
minimums[W_RS] = W_RS_min
crosses = dict()
crosses[W_BL] = W_RM
crosses[W_SL] = W_RS

W, f, F, t_s, h, b, B = symbols("W, f, F, t_s, h, b, B")
data[W] = (f*h)/10+(t_s*h**2)/3000*(1+100*(F-f)/(100*F+t_s*h))

def calcOneModulus(themodulus,pressure,distance,span):
    w=data[themodulus].subs(P,pressure)
    w=w.subs(data)
    w=w.subs(e,distance)
    w=w.subs(l,span)
    w=w.subs(data)
    return w

def calcStiffenerHeight(w,themodulus, layers,span):
    m=data[W].subs(f,7*0.7/10*8).subs(t_s,7*0.7).subs(F,layers*0.7/10*min(span/20,30)).subs(data)-w
    height = solve(m)[2].as_real_imag()
    assert(height[1]<0.00001)
    m=data[W].subs(f,7*0.7/10*8).subs(t_s,layers*0.7/2).subs(F,layers*0.7/10*min(span/20,30)).subs(data)-w*2
    height2 = solve(m)[2].as_real_imag()
    assert(height2[1]<0.00001)
    print " %s: %.2f, %.2f, %.2f, %.2f, %.2f"%(themodulus,w,sqrt(6*w/0.35), sqrt(6*w/0.49), height[0]/10.0, height2[0]/10.0)

def sectionModulus(label,modulus,pressure,distance,span,layers=5):
    ws=[]
    for themodulus in [modulus, minimums[modulus], crosses[modulus], minimums[crosses[modulus]]]:
        w = calcOneModulus(themodulus,pressure,distance,span)
        ws.append((themodulus,w))
    w=max(ws[0][1],ws[1][1])
    themodulus=ws[0][0]
    calcStiffenerHeight(w,themodulus, layers,span)
    w=max(ws[2][1],ws[2][1])
    themodulus=ws[2][0]
    calcStiffenerHeight(w,themodulus, layers,span)

print "keel width:", data[w_keel].subs(data).subs(data)
w = data[G_K].subs(data).subs(data)
print "keel laminate weight:", w, w/300

def laminateWeight(label, pressure, speed_factor, plateWidth, plateLength, header=True):
    if header:
        print label, pressure, speed_factor, plateWidth,"x",plateLength
    assert(plateLength>=plateWidth)
    layers=[]
    ws=[]
    for g in (G,G_min):
        w=data[g].subs(P,pressure)
        w=w.subs(data)
        w=w.subs(a,plateWidth)
        w=w.subs(b,plateWidth)
        w=w.subs(l,plateLength)
        w=w.subs(F_v,speed_factor)
        w=w.subs(data)
        ws.append(w)
    w=max(ws)
    c = ceiling(w/300)
    print " G: %.2f, %.2f, %d, %.2f"%(w,w/300.0, c, c*0.7)
    layers.append(c)
    return max(layers)


def weightAndStiffeners(label, pressure, speed_factor, plateWidth, plateLength, modulus):
    print label, modulus, pressure, speed_factor, plateWidth,"x",plateLength
    layers = laminateWeight(label, pressure, speed_factor, plateWidth, plateLength, header=False)
    sectionModulus(label, modulus, pressure, plateWidth, plateLength/1000, layers)

print "---------------- laminate weights -----------"
weightAndStiffeners("bottom fore main side", P_dbsf, F_vb, 450.0, 500.0, W_BL)
weightAndStiffeners("side fore main", P_dssf, F_vs, 600.0, 640.0, W_SL)
weightAndStiffeners("bottom aft main", P_dbsa, F_vb, 440.0, 640, W_BL)
weightAndStiffeners("bottom aft main under cockpit", P_dbsa, F_vb, 440.0, 575, W_BL)
weightAndStiffeners("side aft main", P_dssa, F_vs, 600.0, 620, W_SL)
weightAndStiffeners("bottom fore ama", P_dbsf, F_vb, 380, 550, W_BL)
weightAndStiffeners("side fore ama", P_dssf, F_vb, 550, 550, W_SL)
weightAndStiffeners("bottom aft ama", P_dbsa, F_vb, 380, 550, W_BL)
weightAndStiffeners("side aft ama", P_dssa, F_vb, 550, 550, W_SL)
l_ = sqrt((1.30-0.35)**2+(2.515-2.7052)**2)*1000
laminateWeight("door", P_dd, 1, 341, l_)
laminateWeight("door top", P_dd, 1, 300, 3300-2700)
laminateWeight("cabin top", P_dd, 1, 548, 3840-2700)
laminateWeight("cabin entry", P_dd, 1, 794-284, l_)
laminateWeight("deck aft", P_dd, 1, 940-450, (3.84-2.6)*1000)
laminateWeight("deck aft2", P_dd, 1, 940-450, 1750)
laminateWeight("deck fore", P_dd, 1, 1000, (6.0-4.05)*1000)
weightAndStiffeners("aft", P_dbsa, F_vb, 950-450, 710,W_BL)
laminateWeight("cockpit deck", P_dd, 1, 550, 1000)
l_ = sqrt((714.0-548)**2+(224-799)**2)
laminateWeight("cockpit wall", P_dd, 1, l_, 1000)
laminateWeight("cabin side", P_dd, 1, 1300-800+100, 3840-2600+200)
