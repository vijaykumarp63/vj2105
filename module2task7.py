import turtle
import math
s=turtle.Turtle()
bob=turtle.Turtle()
ace=turtle.Turtle()

def square(bob):
	for i in range(4):
		bob.fd(100)
		bob.rt(90)
square(bob)

def polygon(ace,n,length):
	angle=360.0/n
	for i in range(n):
		ace.fd(length)
		ace.lt(angle)
polygon(ace,8,45)

def circle(ace,r):
	circumference=2*math.pi*r
	n=50
	length=circumference/n
	polygon(ace,30,10)
circle(ace,10)

def arc(s,r,angle):
	arc_length=2*math.pi*r*angle/360
	n=int(arc_length/3)+1
	test_length=arc_length/n
	test_angle=float(angle)/n

	for i in range(n):
		s.fd(test_length)
		s.rt(test_angle)
arc(s,45,90)
turtle.mainloop()
			

