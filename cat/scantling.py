#!/usr/bin/python

cm=0.01 #cm in m
g=10 #gravitation

#Beam length in m
L=4
#ama max weight in kg
m=440

#we count the two side in one
print "fore beam have two 3x20 flat irons added to each vertical plane of angle steels" 
a1=0.6*cm*3
b1=1.7*cm
l1=(33.94+0.3+1.7/2)*cm

a2=4*cm
b2=0.3*cm
l2=(33.94+0.3/2)*cm

a3=0.6*cm*3
b3=1.7*cm
l3=(3.94-1.7/2)*cm

a4=4*cm
b4=0.3*cm
l4=(3.94+0.3/2)*cm

def Irectangular(vertical,horizontal):
    return vertical**3*horizontal/3

I1=Irectangular(a1,b1)
I2=Irectangular(a2,b2)
I3=Irectangular(a3,b3)
I4=Irectangular(a4,b4)

print "I values for parts:"
print I1,I2,I3,I4

A1=a1*b1
A2=a2*b2
A3=a3*b3
A4=a4*b4

y=(l1*A1+l2*A2+l3*A3+l4*A4)/(A1+A2+A3+A4)

print "centerline:"
print y/cm

Y=19.09*cm
assert(abs(y-Y)<0.0001)
y1=l1-y
y2=l2-y
y3=l3-y
y4=l4-y

print "distances from centerline:"
print y1,y2,y3,y4

def Ipara(Ipart,offset,area):
    return Ipart+offset**2*area

I = Ipara(I1,y1,A1)+Ipara(I2,y2,A2)+Ipara(I3,y3,A3)+Ipara(I4,y4,A4)

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

##################################aft beam############################
#longitudinal center of buoyancy
Lcb=3.43
Lbeam1=4.15
Lbeam2=1.05

Lbb=Lbeam1-Lbeam2
Lcp=Lbeam1-Lcb

#Beam length in m
L=4
#ama max weight in kg
m=440

#aft beam nominal load
m=m*Lcp/Lbb

#we count the two side in one
a1=0.6*cm
b1=1.7*cm
l1=(33.94+0.3+1.7/2)*cm

a2=4*cm
b2=0.3*cm
l2=(33.94+0.3/2)*cm

a3=0.6*cm
b3=1.7*cm
l3=(3.94-1.7/2)*cm

a4=4*cm
b4=0.3*cm
l4=(3.94+0.3/2)*cm

def Irectangular(vertical,horizontal):
    return vertical**3*horizontal/3

I1=Irectangular(a1,b1)
I2=Irectangular(a2,b2)
I3=Irectangular(a3,b3)
I4=Irectangular(a4,b4)

print "I values for parts:"
print I1,I2,I3,I4

A1=a1*b1
A2=a2*b2
A3=a3*b3
A4=a4*b4

y=(l1*A1+l2*A2+l3*A3+l4*A4)/(A1+A2+A3+A4)

print "centerline:"
print y/cm

Y=19.09*cm
assert(abs(y-Y)<0.0001)
y1=l1-y
y2=l2-y
y3=l3-y
y4=l4-y

print "distances from centerline:"
print y1,y2,y3,y4

def Ipara(Ipart,offset,area):
    return Ipart+offset**2*area

I = Ipara(I1,y1,A1)+Ipara(I2,y2,A2)+Ipara(I3,y3,A3)+Ipara(I4,y4,A4)

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

