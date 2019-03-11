import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model1(U,x,e):
    return [U[1], -1*(U[0] + (e * (U[0]**3)))]

def prob1_2():
	U0 = [0,1]
	epsilon = [-0.1, -0.2, -0.3, -0.4, -0.499, -1]
	ts = np.linspace(0,20,150)
	for i in range(1,7):
		Us = odeint(model1, U0, ts, args=(epsilon[i - 1], ))
		print(f"THe loop {i}")
		plt.subplot(3,2,i)
		plt.plot(ts, Us[:,0])
		plt.title(f"Epsilon = {epsilon[i - 1]}")
		plt.xlabel("time")
		plt.ylabel("y")
		plt.ylim(-2,2)
		plt.grid()
		plt.tight_layout()

	plt.show()
	#print(Us)
	print(Us.shape)
	#plt.savefig('test.png')

def model2(U,t,w):
	y = U[0]
	dy = U[1]

	dyy = -(0.2*dy + (y + (0.2*(y**3)))) + np.cos(w*t)
	return[dy, dyy]


def prob3():
	U0 = [0,0]
	ts = np.linspace(0,60, 600)
	#w = [0.5, 0.6, 0.7, 0.8, 0.9]
	w = [1.2, 1.25, 1.3, 1.35, 1.4]
	for i in range(1,6):
		Us = odeint(model2, U0, ts, args=(w[i-1], ))
		print(f"The loop {i}")
		plt.subplot(3,2,i)
		plt.plot(ts, Us[:,0])
		plt.title(f"w = {w[i - 1]}")
		plt.xlabel("time")
		plt.ylabel("y")
		plt.ylim(-6,6)
		plt.grid()
		plt.tight_layout()

	plt.show()


if __name__ == '__main__':
	#prob1_2()
	prob3()