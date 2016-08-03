#!/usr/bin/python
from math import *

g=10 #gravitation

#Beam length in m
L=4.624
#ama max weight in kg
m1=500
#mainhull max weight in kg
m2=500

h=0.15
w=0.2
l=4.9/1000
x=2*l*sqrt(1/4+h**2/w**2)
k=l/h*sqrt(w**2/4+h**2)

a1=l
b1=w+2*k
l1=x+h

a2=h
b2=2*k
l2=x

a3=x
b3=2*k
l3=0

def Irectangular(vertical,horizontal):
    return vertical**3*horizontal/3

def Itriangular(vertical,horizontal):
    return vertical**3*horizontal/12

I1=Irectangular(a1,b1)
I2=Irectangular(a2,b2)
I3=Itriangular(a3,b3)

print "I values for parts:"
print I1,I2,I3

A1=a1*b1
A2=a2*b2
A3=a3*b3/2

y=(l1*A1+l2*A2+l3*A3)/(A1+A2+A3)

print "centerline:"
print y

y1=l1-y
y2=l2-y
y3=l3-y

print "distances from centerline:"
print y1,y2,y3

def Ipara(Ipart,offset,area):
    return Ipart+offset**2*area

I = Ipara(I1,y1,A1)+Ipara(I2,y2,A2)+Ipara(I3,y3,A3)

print "Area moment of inertia for whole beam:"
print I

M=(L*m1 + L/2*m2)*g # L/2 is mainhull position

print "Moment (Nm):"
print M

stress = M*y/I

print "stress (N/m2, a.k.a. Pa), and in MPa:"
print stress, stress/1000000
print "(strength >= 85 MPa, )"
