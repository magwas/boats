#!/usr/bin/python

mm=0.001 #mm in m
g=10 #gravitation

#Beam length in m
L=2
#ama max weight in kg
m=500

a1=300*mm
b1=1*mm
l1=150.5*mm

a2=1.4142*mm
b2=149.2929*mm
l2=148*mm

a3=16*mm
b3=4*mm
l3=142.3431*mm

a4=5.6569*mm
b4=7.3137*mm
l4=74.6464*mm


b5=8.4853*mm
l5=9.8995*mm

b6=11.3137*mm
l6=8.4853*mm


def Irectangular(vertical,horizontal):
    return vertical**3*horizontal/3

I1=Irectangular(a1,b1)
I2=Irectangular(a2,b2)
I3=Irectangular(a3,b3)
I4=Irectangular(a4,b4)
I5=Irectangular(a4,b5)
I6=Irectangular(a4,b6)

print "I values for parts:"
print I1,I2,I3,I4,I5,I6

A1=a1*b1
A2=a2*b2
A3=a3*b3
A4=a4*b4
A5=a4*b5
A6=a4*b6

y=(l1*A1+l2*A2*2+l3*A3*2+l4*A4*2+l5*A5+l6*A6)/(A1+A2*2+A3*2+A4*2+A5+A6)

print "centerline:"
print y/mm

Y=127.3287*mm
assert(abs(y-Y)<0.0001)
y1=l1-y
y2=l2-y
y3=l3-y
y4=l4-y
y5=l5-y
y6=l6-y

print "distances from centerline:"
print y1,y2,y3,y4,y5,y6

def Ipara(Ipart,offset,area):
    return Ipart+offset**2*area

I = Ipara(I1,y1,A1)+2*Ipara(I2,y2,A2)+2*Ipara(I3,y3,A3)+2*Ipara(I4,y4,A4)+Ipara(I5,y5,A5)+Ipara(I6,y6,A6)

print "Area moment of inertia for whole beam:"
print I

M=L*m*g

print "Moment (Nm):"
print M

ymax=Y 
stress = M*ymax/I

print "stress (N/m2, a.k.a. Pa), and in MPa:"
print stress, stress/1000000
print "(tensile strength for steel is >> 200 MPa)"
