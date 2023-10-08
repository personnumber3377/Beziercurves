

import numpy as np
import math
import turtle

def binom_coeff(a,b):

	return (math.factorial(a))/(math.factorial(b)*(math.factorial(a-b)))


def generate_bezier_point(t, points):

	# https://en.wikipedia.org/wiki/B%C3%A9zier_curve#Explicit_definition

	assert t <= 1
	assert t >= 0

	cur_point = np.array([0.0,0.0])

	n = len(points)-1 # We need to do this because the indexing in the wikipedia page is a bit weird.
	for i in range(n+1): # Same here

		term = (binom_coeff(n,i))*(((1.0-t)**(n-i))*(t**i))*points[i]
		print("points[i] == "+str(points[i]))
		cur_point += term

	return cur_point



def draw_point(point, turt, scalefactor):
	turt.goto(point[0]*scalefactor, point[1]*scalefactor)
	turt.pendown()
	turt.circle(10)
	turt.penup()


def main():

	t = 0.0
	bezier_points = [np.array([0.0,0.0]), np.array([1.0,1.0]), np.array([2.0,0.0])]
	scalefactor = 400
	timesteps = 10000

	d_t = 1.0/timesteps
	turt = turtle.Turtle()
	turtle.speed(0)
	turtle.clear()
	turt.clear()
	turtle.tracer(0)

	for _ in range(timesteps):
		# print("t == "+str(t))
		cur_point = generate_bezier_point(t, bezier_points)

		t += d_t
		print("t == "+str(t))
		turt.goto(cur_point[0]*scalefactor,cur_point[1]*scalefactor)
		turt.dot()

		for point in bezier_points:
			draw_point(point, turt, scalefactor)
		turtle.update()
		turtle.clear()
		turt.clear()

		
		#turt.update()

	return 0




if __name__=="__main__":

	exit(main())
