#!/usr/bin/python

mm=0.001
l1=300*mm
l2=212.132*mm
l3=20*mm
l4=15*mm
d1=2*mm
d2=4*mm
y1=37.0274*mm
y2=47.5126*mm
y3=33.0229*mm
y4=98.8305*mm
y5=50.5126*mm
a=11.313*mm
b=5.6569*mm
a1=2.8284*mm
b1=2.8284*mm
dl1=7.0711*mm

y=108.73*mm
M=4000

I0=(a**3)*b/3
I1=(a1**3)*b/12

#I for one flat rod
If = I0+2*(I1+(dl1**2)*a1*b/2)
Af = l3*d2

print "If=%s"%(If,)

#I for top element
It=(d1**3)*l1/3
At=l1*d1

#I for side element, lower approximation
Is=((l4-4*mm)**3)*b1/3

print "Is=%s"%(Is,)
#I for all the beam

I=If*6 + Af*(2*(y1**2)+2*(y2**2)+2*(y4**2)) + It+2*Is+At*((y5**2)+2*(y4**2))

print "I=%s"%(I,)

E=-M*y/I

print "E=%s"%(E,)

