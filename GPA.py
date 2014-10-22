#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy.random import *
import matplotlib.pyplot as plt
import numpy

GPA = []

#Standard Deviation
def std_dev(*n):
    print "Input your GPA"
    x = input()
    std = numpy.round_(50 + 10 * (x - numpy.average(n)) / numpy.std(n))
    print "Your GPA's Standard deviation:", std

#Simulation
for i in range(100000):
    tmp = normal(1.98, 0.78)
    if tmp > 0 and tmp < 4:
        GPA.insert(i, tmp)

#Result
print "　Average:",numpy.average(GPA)
print std_dev(GPA)
plt.hist(GPA)
plt.show()