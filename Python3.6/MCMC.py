# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:26:21 2020

————————————————
版权声明：本文为CSDN博主「fjssharpsword」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fjssharpsword/article/details/80336985

@author: hjiang
"""

import random
from scipy.stats import norm
import matplotlib.pyplot as plt
 
def cauchy(theta):#从柯西分布p中采样数据
    y = 1.0 / (1.0 + theta ** 2)
    return y
 
T = 5000
sigma = 1
thetamin = -30
thetamax = 30
theta = [0.0] * (T+1)
theta[0] = random.uniform(thetamin, thetamax)
 
t = 0
while t < T:
    t = t + 1
    
    theta_star = norm.rvs(loc=theta[t - 1], scale=sigma, size=1, random_state=None)#从已知正态分布q中生成候选状态
 
    alpha = min(1, (cauchy(theta_star[0]) / cauchy(theta[t - 1])) )
 
    u = random.uniform(0, 1)
    if u <= alpha:#接受
        theta[t] = theta_star[0]
    else:
        theta[t] = theta[t - 1]
 
#print (theta)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212) 
plt.sca(ax1)
plt.ylim(thetamin, thetamax)
plt.plot(range(T+1), theta, 'g-')
plt.sca(ax2)
num_bins = 50
plt.hist(theta, num_bins, normed=1, facecolor='red', alpha=0.5)
plt.show()
