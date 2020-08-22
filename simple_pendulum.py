import matplotlib.pyplot as plt
import numpy as np


class Simple_pendulum(object):

    def __init__(self, omega_0 = 0, theta_0 = 10, eta=0.01, n_iter=10):
        self.omega_0 = omega_0
        self.theta_0 = theta_0
        self.eta = eta
        self.n_iter = n_iter
    
    
    def midpoint(self,alpha):
        
        self.time_ = np.zeros(self.n_iter)
        self.omega_ = np.zeros(self.n_iter)
        self.theta_ = np.zeros(self.n_iter)
        self.omega_[0] = self.omega_0
        self.theta_[0] = self.theta_0*np.pi/180.0
        
        for i in range(self.n_iter-1):
            self.time_[i+1] = self.time_[i] + self.eta
            self.omega_[i+1] = self.omega_[i] + self.eta*alpha(self.theta_[i])
            self.theta_[i+1] = self.theta_[i] + 0.5*self.eta*(self.omega_[i]+self.omega_[i+1])
        return self

def alpha(x):

    return -np.sin(x)

time=Simple_pendulum(omega_0 = 0, theta_0 = 10, eta=0.1, n_iter=300).midpoint(alpha).time_
theta=Simple_pendulum(omega_0 = 0, theta_0 = 10, eta=0.1, n_iter=300).midpoint(alpha).theta_
plt.plot(time,theta*180/np.pi,lw=3,color='green')
plt.xlabel('time(s)',size=13)
plt.ylabel('angle (deg)',size=13)
plt.title('Midpoint Method',size=13)
plt.show()

        
        
