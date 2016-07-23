#!/usr/bin/python
from __future__ import division
from sympy import *

cm=0.01 #cm in m
g=10 #gravitation

#Beam length in m
L=4.62
#ama max weight in kg + 2 people
m=440

#we count the two side in one
print "fore beam have two 3x20 flat irons added to each vertical plane of angle steels" 
a5=20*cm
b5=0.15*cm
l5=(23.93+2.0)*cm

a1=0.6*cm #*3
b1=1.7*cm
l1=(33.93+0.3)*cm

a2=4*cm
b2=0.3*cm
l2=(23.93)*cm

a3=0.6*cm*3
b3=1.7*cm
l3=(2.15)*cm

a4=4*cm
b4=0.3*cm
l4=(2.09+0.15+1.7)*cm

a6=20*cm
b6=0.15*cm
l6=(2.09)*cm

def Irectangular(vertical,horizontal):
    return vertical**3*horizontal/3

I1=Irectangular(a1,b1)
I2=Irectangular(a2,b2)
I3=Irectangular(a3,b3)
I4=Irectangular(a4,b4)
I5=Irectangular(a5,b5)
I6=Irectangular(a6,b6)

print "I values for parts:"
print I1,I2,I3,I4, I5

A1=a1*b1
A2=a2*b2
A3=a3*b3
A4=a4*b4
A5=a5*b5
A6=a6*b6

y=(l1*A1+l2*A2+l3*A3+l4*A4+l5*A5+l6*A6)/(A1+A2+A3+A4+A5+A6)

print "centerline:"
print y/cm

#Y=19.0477*cm
y1=l1-y
y2=l2-y
y3=l3-y
y4=l4-y
y5=l5-y

print "distances from centerline:"
print y1,y2,y3,y4, y5

def Ipara(Ipart,offset,area):
    return Ipart+offset**2*area

I = Ipara(I1,y1,A1)+Ipara(I2,y2,A2)+Ipara(I3,y3,A3)+Ipara(I4,y4,A4)+Ipara(I5,y5,A5)

print "Area moment of inertia for whole beam:"
print I

M=L*m*g

print "Moment (Nm):"
print M

stress = M*y/I

print "stress (N/m2, a.k.a. Pa), and in MPa:"
print stress, stress/1000000
print "(tensile strength for steel is >> 200 MPa)"

##################################aft beam############################
#longitudinal center of buoyancy
Lcb=3.43
Lbeam1=4.15
Lbeam2=1.05

Lbb=Lbeam1-Lbeam2
Lcp=Lbeam1-Lcb

#aft beam nominal load
m2=m*Lcp/Lbb

y=(l1*A1+l2*A2+l3*A3+l4*A4)/(A1+A2+A3+A4)

print "centerline:"
print y/cm

y1=l1-y
y2=l2-y
y3=l3-y
y4=l4-y

print "distances from centerline:"
print y1,y2,y3,y4

I = Ipara(I1,y1,A1)+Ipara(I2,y2,A2)+Ipara(I3,y3,A3)+Ipara(I4,y4,A4)

print "Area moment of inertia for whole beam:"
print I

M=L*m2*g

print "Moment (Nm):"
print M

stress = M*y/I

print "stress (N/m2, a.k.a. Pa), and in MPa:"
print stress, stress/1000000
print "(tensile strength for steel is >> 200 MPa)"


#################### mast ##################

Lmast = 2.9
r1 = 7.5*cm
r2 = 5.42*cm
I = pi/4*(r1**4-r2**4)
stress = 80*1000000
F =symbols("F")
M=Lmast*F
eq_stress = M*r1/I - stress

f = solve(eq_stress)[0]
print "max force at mast top (N):", f
print "bending moment: Nm", M.subs(F,f) 
