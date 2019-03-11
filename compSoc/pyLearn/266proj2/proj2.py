import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model2(Q,t,w):
	y = Q[0]
	dy = Q[1]

	dyy = -(4*dy + (5*y)) + (10* np.cos(w*t))
	return[dy, dyy]


def prob2():
	U0 = [0,0]
	ts = np.linspace(0, 80, 800)
	w = [0, 0.5, 1, 2, 5, 10, 15, 20, 25]
	for i in range(1,10):
		Us = odeint(model2, U0, ts, args=(w[i-1], ))
		print(f"The loop {i}")
		plt.subplot(3,3,i)
		plt.plot(ts, Us[:,0])
		plt.title(f"w = {w[i - 1]}")
		plt.xlabel("time")
		plt.ylabel("y")
		plt.ylim(-4,4)
		plt.grid()
		plt.tight_layout()

	plt.savefig('problem2.png')
	plt.show()

def model1(Q,t,w):
	y = Q[0]
	dy = Q[1]

	dyy = -(4*dy + (5*y)) + (10* np.cos(w*t))
	return[dy, dyy]


def prob1():
	U0 = [0,0]
	ts = np.linspace(0, 80, 800)
	w = [0, 0.5, 1.2, 4, 8, 16]
	for i in range(1,7):
		Us = odeint(model1, U0, ts, args=(w[i-1], ))
		print(f"The loop {i}")
		plt.subplot(3,2,i)
		plt.plot(ts, Us[:,0])
		plt.title(f"w = {w[i - 1]}")
		plt.xlabel("time")
		plt.ylabel("y")
		plt.ylim(-4,4)
		plt.grid()
		plt.tight_layout()

	plt.savefig('problem1.png')
	plt.show()

if __name__ == '__main__':
	#prob1_2()
	prob2()