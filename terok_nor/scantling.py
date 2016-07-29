#!/usr/bin/python
from __future__ import division
import sys
from sympy import *

mm, m, cm = symbols('mm, m, cm')
data = {}

L, L_wl, L_wl_main, L_wl_ama, L_main, L_ama, v, b, b_main, b_ama, a, a_main, a_ama, l, l_main, l_ama, R = symbols("L, L_wl, L_wl_main, L_wl_ama, L_main, L_ama, v, b, b_main, b_ama, a, a_main, a_ama, l,l_main, l_ama, R")

data[L_main] = 7.0
data[L_ama] = 6.314
data[L_wl_main] = 7.0
data[L_wl_ama] = 5.918
data[a_main] = 385.0 #385 mm is recommended
data[a_ama] =  375.0 #375 mm is recommended
#data[b_main] = 300.0
data[b_main] = 1000.0
data[b_ama] = 300.0
data[l_main] = 1000.0
data[l_ama] = 1000.0
data[v] = 10.0
data[R] = (a/l).subs(data)
#R: width/height of unsupported plate panels

P_dbsf, P_dbsa, P_dssf, P_dssa = symbols("P_dbsf, P_dbsa, P_dssf, P_dssa")
P_dbmf, P_dbma, P_dsmf, P_dsma = symbols("P_dbmf, P_dbma, P_dsmf, P_dsma")
F_vb, F_vs, F_vf, F_P, P_dd, F_p, F_vl, F_vsf, F_vsl = symbols("F_vb, F_vs, F_vf, F_p, P_dd, F_p, F_vl, F_vsf, F_vsl")

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
data[F_vsf] = (0.1*sqrt(v/sqrt(L_wl))+0.52)*(1.19-0.01*L)
data[F_vsl] = (0.14*sqrt(v/sqrt(L_wl))+0.47)*(1.07-0.008*L)

G_WB, G_WS, G_WS_min, G_WB_min, G_WF, G_WK = symbols("G_WB, G_WS, G_WS_min, G_WB_min, G_WF, G_WK")

P_dBS, P_dSS = symbols("P_dBS, P_dSS")

data[G_WB] = 1.57*b*F_p*F_vb*sqrt(P_dBS)
data[G_WB_min] = 1.1*(350+5*L)*sqrt(P_dBS)
data[G_WS] = 1.57*b*F_p*F_vs*sqrt(P_dSS)
data[G_WS_min] = 1.1*(350+5*L)*sqrt(P_dSS)
data[G_WF] = 1.7*(350+5*L)*sqrt(2.4*L+28)
data[G_WK] = 1.7*(350+5*L)*sqrt(3.3*L+66.5)

w_keel = symbols("w_keel,")

data[w_keel] = 25*L+300

t,t_min,P = symbols("t, t_min, P")

data[t] = 1.62*a*sqrt(P)
data[t_min] = 0.9*sqrt(L)

main = {}
for k,v in ((L,L_main),(b,b_main),(a,a_main),(l,l_main),(L_wl,L_wl_main)):
    main[k] = data[v]

ama = {}
for k,v in ((L,L_ama),(b,b_ama),(a,a_ama),(l,l_ama),(L_wl,L_wl_ama)):
    ama[k] = data[v]

fore = {
    P_dBS: data[P_dbsf],
    P_dSS: data[P_dssf],
}

aft = {
    P_dBS: data[P_dbsa],
    P_dSS: data[P_dssa],
}

for k,v in data.items():
    print "-------------------------------"
    print k
    pprint(v)
    if float!=type(v):
        print v.subs(main).subs(fore).subs(data)

for (length,b_, a_, l_, L_wl_) in [(L_main,b_main,a_main,l_main, L_wl_main), (L_ama,b_ama,a_ama,l_ama, L_wl_ama)]:
    print length
    for weight in [G_WB, G_WS, G_WS_min, G_WB_min, G_WF, G_WK, t]:
        print " ",weight
        for (dbs,dss) in [(P_dbsf, P_dssf), (P_dbsa,P_dssa)]:
            print "  ", dbs
            w = data[weight]
            #pprint(w)
            w = w.subs(P_dBS,dbs).subs(P_dSS,dss).subs(L,length)
            #pprint(w)
            w = w.subs(b, b_).subs(data).subs(L,length).subs(data).subs(a,a_)
            #pprint(w)
            w = w.subs(L_wl,L_wl_).subs(l,l_).subs(data)
            print "   ", w, w/300.0
    for p in [P_dbsf, P_dssf]:
        print " t", p
        thickness = data[t].subs(P,p).subs(data).subs(L,length).subs(a,a_).subs(data)
        print "   ", thickness
            
