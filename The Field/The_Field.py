# Code snippets for tasks from Chapter 1: The Field
# in Coding the Matrix

import sys
sys.path.append('C:\\Users\\jksim\\PycharmProjects\\Coding The Matrix\\The Field')

import os
os.chdir('C:\\Users\\jksim\\PycharmProjects\\Coding The Matrix\\The Field')
from plotting import plot

import image

# note: the module 'plotting' does not run correctly for me in Pycharm
# I am including the code snippets here, but I was able to run this code
# directly in the python command line and in the Pycharm Python Console.
# I had to import sys and use sys.path.append()
# to access the directory containing the plotting module
# and the image module (see imports above)

# Task 1.4.1: Plot the set of points S using the plot command


S = [2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j]
# from plotting import plot
plot(S,4)
# when run from python terminal this opens a window that
# plots the points above in the complex plane
# note: I had to import sys and append the file path to use the plotting module as it is not native to python


# Task 1.4.3: Create a plot using a comprehension that translates S
# by the complex number 1+2j; that is 1 unit right & 2 units up

# note that the list comprehension is created in the first argument of plot
plot([x+(1+2j) for x in S],4)


# Task 1.4.7: Create a new plot that shrinks the points from the previous task
# by a factor of 1/2

plot([0.5*(x+(1+2j)) for x in S])

# Task 1.4.8: Create a new plot that rotates S by 90 degrees (counterclockwise)
# and shrinks by a factor of 1/2. The transformation should use a single complex number

plot([x*0.5j for x in S],4)

# Task 1.4.9: Using a comprehension create a new plot in which the points of S are
# rotated by 90 degrees, scaled by 1/2, then shifted down by 1 unit and right 2 units.
# Use a comprehension where the points are multiplied by one complex number and added to another

# rotate 90 degrees, scale by 1/2, shift down 1, right 2

plot([(x*0.5j)+(2-1j) for x in S],4)

# Task 1.4.10: Download the image.py module and image png file From the resources page.
# import the procedure file2image from the image module
# run file2image on the file an assign its output to the variable "data"
# file2image converts the image to a set of gray scaled points that can be plotted
# data is a list of lists. data[y][x] contains the intensity of pixel at point (x,y)
# See the textbook for more details. See errata wrt color2gray
# plot the image. I called the list 'data' instead of 'pts'


# convert file to image
data = image.file2image('C:\\Users\\jksim\\PycharmProjects\\Coding The Matrix\\The Field\\img01.png')

# covert image to gray image
gray_image = image.color2gray(data)

#plot scale needs to be adjusted here. use max absolute value of plotted pixels.
# Errata suggested scale of 255

# don't really need this but it helped me figure out how to plot the image
pixels = [(x,y) for y in range(len(gray_image)) for x in range(len(gray_image[y])) if gray_image[y][x]<120]

#this plots the image in the wrong orientation. Not sure why
# image is reflected about horizontal line through middle of the window containing image
# plot([x+y*1j for x in range(len(gray_image[y]) for y in range(len(gray_image)) if gray_image[y][x] < 120],4 )

# ***THIS PLOTS THE CORRECT IMAGE***
# ***this reflects the image and gives the desired image orientation except it is in color...
plot([x+(189-y)*1j for y in range(len(gray_image)) for x in range(len(gray_image[y]))
      if gray_image[y][x] < 120],248 )


# Task 1.4.11: Write a python procedure f(z) that take a complex number z as an argument
# so that when f(z) is applied to each number in S, the set of resulting numbers is centered
# at the origin.
# Write a comprehension in terms of S and f whose value is the set of translated points
# then plot them

# By symmetry the middle point of S is at (2.5, 1.5).
# So use complex number -1*(2.5 +1.5*j)

S = [2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j]

#define translating function
def f(z): return z - complex(2.5, 1.5)

#create list of translated points
[f(z) for z in S]

# plot points; again doesn't work in Pycharm
plot([f(z) for z in S],4)

# Task 1.4.12: Repeat Task 1.4.8 for the set of points from the gray_image in Task 1.4.10
# Task 1.4.8 rotated 90 degrees and scaled by 0.5
plot([(x*0.5j)+(-1+2j) for x in S],4)

# Apply transformation from 1.4.8 to x + (189-y)*j in the comprehension
# but now iterate over the new points from 1.4.10
# change scale also


plot([0.5j*(x+(189-y)*1j)+(2-1j) for y in range(len(gray_image))
     for x in range(len(gray_image[y])) if gray_image[y][x] < 120 ],248)

# Task 1.4.18: Write a comprehension that rotates the elements of S by pi/4
# plot the comprehension

# rotate by pi/4

from math import e, pi

#rotate each element of  S by pi/4
# S = [2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j]
# [x*e**((pi/4)*1j) for x in S]
plot([x*e**((pi/4)*1j) for x in S],4)

# Task 1.14.19: Write a comprehension that rotates the elements of
# the gray_scale image by pi/4
# multiple pixels in original comprehension by e**((pi/4)*1j)

plot([(x+(189-y)*1j)*e**((pi/4)*1j) for y in  range(len(gray_image))
      for x in range(len(gray_image[y])) if gray_image[y][x] < 120],248 )

# Task. 1.4.20: Write a comprehension that transforms the gray_image by
# centering it at the origin, rotating by pi/4, and scaling by 1/2

# len(gray_image[0]) = 166, max x coordinate
# len_gray_image = 189; max y coordinate
# "corners of the gray_image are (0,0), (166,0), (0,189), (166,189)
# center of image is (166/2,189/2) by symmetry
# translate by vector from symmetry to origin

plot([((x+(189-y)*1j) - complex(166/2, 189/2))*e**((pi/4)*1j)*0.5
      for y in range(len(gray_image)) for x in range(len(gray_image[y]))
      if gray_image[y][x] < 120],248 )

## Note: yet to complete problem 1.5.1 (cryptograph problem)
# still figuring it out :)

