# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:45:29 2020

@author: hjiang
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

points_n = 200
clusters_n = 3
iteration_n = 20
points = tf.constant(np.random.uniform(0, 10, (points_n, 2)))
centroids = tf.constant(tf.slice(tf.compat.v1.random_shuffle(points), [0, 0], [clusters_n, -1]))

points_expanded = tf.expand_dims(points, 0)

@tf.function
def update_centroids(points_expanded, centroids):
    centroids_expanded = tf.expand_dims(centroids, 1)
    
    distances = tf.reduce_sum(tf.square(tf.subtract(points_expanded, centroids_expanded)), 2)
    assignments = tf.argmin(distances, 0)
    means = []
    for c in range(clusters_n):#把每一类的means 更新
        ruc = tf.reshape(tf.where(tf.equal(assignments, c)), [1,-1])#找类别
        ruc = tf.gather(points, ruc)#挑出来
        ruc = tf.reduce_mean(ruc, axis=[1])#求此类的均值
        means.append(ruc)#
        new_centroids = tf.concat(means, 0)
    return new_centroids, assignments

for _ in range(iteration_n):
    centroids, assignments = update_centroids(points_expanded, centroids)


plt.scatter(points[:, 0], points[:, 1], c=assignments, s=50, alpha=0.5)
plt.plot(centroids[:, 0], centroids[:, 1], 'kx', markersize=15)
plt.show()