#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 12:20:10 2021

@author: emre
"""

# ---------
# Part 1: Some Elementary Python Tasks
print("\n")
print("Part 1: Some Elementary Python Tasks")
print("\n")

import csv     # imports the csv module
import sys     # imports the sys module

f = open('TB_burden_countries_2014-09-29.csv') # opens the csv file
data = csv.reader(f)

r = 0 # row count
c = 0 # non-null item count in the column
t = 0 # total in the column
e = 0 # empty values

# use next() to skip the first line in csv
next(f)

# row count and column average calculation
for row in data:
    r = r + 1
    if row[11] == "": # if statement to skip blanks in the data
        e = e + 1
        #print(row[11])
    else:
        t = t + float(row[11])
        c = c + 1

# calculate the average of the column
m = t / c

# row count in csv file
print("1. The row count in the data is", r)

# average of e_prev_num_lo column
print("2. The average e_prev_num_lo is", round(m, 2))

# column average calculation based on years
d = open('TB_burden_countries_2014-09-29.csv') # opens the csv file
data2 = csv.reader(d)

co = 0 # 1991 value counts
cn = 0 # 2011 value counts

to = 0 # 1991 total
tn = 0 # 1991 total

e2 = 0

for row2 in data2:
    if row2[11] == "": # if statement to skip blanks in the data
        t = t
        e2 = e2 + 1
        #print(row[11])
    else:
        if row2[5] == "1990":
            to = to + float(row2[11])
            co = co + 1
            #print(co)
        elif row2[5] == "2011":
            tn = tn + float(row2[11])
            cn = cn + 1
            #print(cn)

mo = to / co # 1991 average
mn = tn / cn # 2011 average
            
# average of e_prev_num_lo column
print("3. The 1990 average e_prev_num_lo column is", round(mo, 2))

# average of e_prev_num_lo column
print("3. The 2011 average e_prev_num_lo column is", round(mn, 2))

print("\n")

# ---------
# Part 2: Numpy
print("Part 2: Numpy")
print("\n")

import numpy as np

# task 1
array1 = np.arange(5, 16, 1)
print("1. The array of int ranging from 5-15:", array1, sep = "\n")
print("\n")

# task 2
array2 = np.linspace(0, 23, 7)
print("2. The array containing 7 evenly spaced numbers between 0 and 23:", np.round(array2, 2), sep = "\n")
print("\n")

# task 3
np.random.seed(5) # setting random seed for reproducible random results
array3 = np.random.uniform(-1,1,100)
print("3. The numpy array with values between -1 and 1 that follow a uniform data distribution:", np.round(array3, 2), sep = "\n")
print("\n")

# task 4
import matplotlib.pyplot as plt
plt.style.use('ggplot')

hist = plt.hist(array3, bins = 10)

print("4. The histogram arrays (x and y axis) for uniformly distributed array (histogram itself will also appear in the output):", hist, sep = "\n")
print("\n")

# task 5
array4 = np.random.randint(5, size=(10))
array5 = np.random.randint(10, size=(10))

print("5. The first ten element array:", array4, sep = "\n")
print("\n")

print("5. The second ten element array:", array5, sep = "\n")
print("\n")

# # task 5 numpy function solution
ed = np.sqrt(np.sum(np.square(array4 - array5)))

print("5. The Euclidean distance between the arrays:", np.round(ed, 2), sep = " ")

# task 5 loop solution as an alternative
total = 0

for i in range(0, 10):
    t = np.power((array4[i] - array5[i]), 2)
    total = total + t

ed_alt = np.sqrt(total)

print("5. The Euclidean distance between the arrays (with loop solution):", np.round(ed_alt, 2), sep = " ")

#committer config change