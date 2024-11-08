# Linear Algebra Coding the Matrix, Edition 1
# Tasks 4.15.2 through 4.15.12 in order

""" A module that performs simple linear transformations of images where images are stored as matrices.
    Information below is taken from image_mat_util module:

    An image is represented by two matrices, representing points and colors.
    The points matrix has row labels {'x', 'y', 'u'} and column labels (0,0) through (w, h), inclusive,
    where (w, h) are the width and height of the original image
    The colors matrix has row labels {'r', 'g', 'b'} and column labels (0,0) through (w-h, h-1).

    The column labels for these matrices represent "lattice points" on the original image.
    For pixel (i,j) in the original image, the (i,j) column in the colors matrix represents
    the pixel color and the (i,j), (i+1, j), (i+1, j+1), and (i, j+1) columns in the points
    matrix represent the boundary of the pixel region
    """

from mat import Mat
from vec import Vec
import image_mat_util
import math
from math import pi



# Note did not test tasks on an image because the file sizes were too large and my computer is slow :(

# Task 4.15.2 write procedure identity() that returns an identity matrix for location vectors
# point at (12,15) has location vector Vec({'x','y','u'},{'x':12, 'y':15, 'u':1})
# color red represented by  Vec({'r','g','b},{'r':1})

def identity():
    """
    This procedure returns an identity location matrix (i.e. the matrix has
    the row and column labels of a location matrix.

    """

    return Mat(({'x','y','u'},{'x','y','u'}),{(i,j):1 for i in {'x','y','u'} for j in {'x','y','u'} if i == j})




# Task 4.15.3 write a procedure translation(alpha,beta) that takes two translation parameters and returns the corresponding
# 3x3 translation matrix. This transformation requires a 3x3 matrix because translations are not linear transformations
# within the plane so no 2x2 transformation matrix exists.

# (x,y,1) are 'homogenous' coordinates. The '1' coordinate is fixed and x and y are transformed within a plane
# (x,y,1) maps to (x+a, y+b, 1)

def translation(alpha,beta):
    """
    This procedure  returns a 3x3 matrix that performs translations in the x and y direction. Translations in the plane
    are not linear transformations. Using homogenous coordinates (x,y,1) to represent a point (x,y) in the plane allows
    the use of 3x3 matrices to perform translations.

    :param alpha: x translation
    :param beta: y translation
    """

    trans_mat = identity() # create identity matrix
    trans_mat['x','u'] = alpha # assign x translation increment
    trans_mat['y','u'] = beta # assign y translation increment
    return trans_mat


# Scaling vector (x,y) to (a*x, b*y) is a linear transformation in the plane thus a 2x2 matrix exists. The
# # x and y coordinates of 3 vector can also be scaled from (x,y,1) to (a*x,b*y,1).

# Task 4.15.4 Write procedure scale(alpha, beta) that takes x and y scale parameters and returns the corresponding
# 3x3 scaling matrix that multiplies a vector (x,y,1).

def scale(alpha, beta) :
    """
    This procedure  returns a 3x3 matrix that performs scaling in the x and y direction. A 3x3 matrix is used to allow
    homogenous coordinates (x,y,1) so that the procedure can be composed with translations in the plane, which require
    the use of 3x3 matrices.

    :param alpha: x scale parameter
    :param beta: y scale parameter
    """

    scale_mat = identity()  # create identity matrix
    scale_mat['x', 'x'] = alpha  # assign x scale parameter
    scale_mat['y', 'y'] = beta  # assign y scale parameter
    return scale_mat


# Task 4.15.5 Write a procedure rotation that takes an angle in radians and returns the corresponding rotation matrix.

def rotation(theta):
    """
    This procedure returns a transformation matrix that rotates theta about (0,0).

    :param theta: angle of rotation (positive is counterclockwise)
    """

    rotation_mat = identity() # create identity matrix
    rotation_mat['x','x'] = math.cos(theta) # set entries for coordinates that correspond to rotation
    rotation_mat['x', 'y'] = -math.sin(theta)
    rotation_mat['y', 'x'] = math.sin(theta)
    rotation_mat['y', 'y'] = math.cos(theta)
    return rotation_mat


# Task 4.15.6 Write a procedure rotation_about(theta,x,y) that takes an angle in radians and returns the corresponding
# rotation matrix.

def rotation_about(theta,x,y):
    """
    This procedure returns a transformation matrix that rotates theta about the point (x,y).

    :param theta: angle of rotation (positive is counterclockwise)
    :param x: x coordinate of center point of rotation
    :param y: y coordinate of center point of rotation
    """
    translate_to_origin = translation(-x,-y) # create matrix that translates center of rotation to origin
    rotate_theta = rotation(theta) # create matrix that rotates theta about the origin
    translate_xy = translation(x,y) # create matrix that translates center of rotation to original point (x,y)
    return translate_xy*rotate_theta*translate_to_origin # composite transformation is product of the matrices (in this order)



# Task 4.15.7: Write a procedure reflect_y() that takes no parameters and returns the matrix which corresponds to a
# reflection about the y-axis. (x,y,1) maps to (-x,y,1)

def reflect_y():
    """This procedure returns a transformation matrix that reflects about the y-axis.
    """
    r_y = identity() # create identity matrix
    r_y['x','x'] = -1
    return r_y

# Task 4.15.8: Write a procedure reflect_x() that takes no parameters and returns the matrix which corresponds to a
# reflection about the x-axis. (x,y,1) maps to (x,-y,1)

def reflect_x():
    """This procedure returns a transformation matrix that reflects about the x-axis.
    """
    r_x = identity() # create identity matrix
    r_x['y','y'] = -1 # assign entry that reflects y coordinate
    return r_x


# Color transformations can be applied using matrix transformations

# Task 4.15.9: Write a procedure scale_color that takes r,g,b scaling parameters and returns the corresponding scaling
# matrix.

# Color vector has labels {'r','g','b'}. These are the row and column labels of the color transformation matrix

def scale_color(r,g,b):
    """
    This procedure returns a transformation matrix that scales the color matrix by the
    given parameters.

    :param r: red scale
    :param g: green scale
    :param b: blue scale
    """
    color_scale_mat = Mat(({'r','g','b'},{'r','g','b'}),{('r','r'):r,('g', 'g'):g,('b', 'b'):b})
    return color_scale_mat

print(scale_color(2,3,4))

# Task 4.15.10: Write procedure grayscale() that returns a matrix that converts a color image to a gray_scale image.
# If the original image had values r,g,b in the color vector, then the grayscale image has
# (77/256)*r + (151/256)*g + (28/256)*b in each color vector
# matrix has same rows. each entry corresponds to scale parameter for color in column label

def grayscale():
    """This procedure returns a transformation matrix that converts a color image to gray scale.
    """

    gray_mat = Mat(({'r','g','b'},{'r','g','b'}),{}) # create empty matrix
    gray_dict = {'r':77/256, 'g':151/256, 'b':28/256} # dict to look up gray scale parameters
    for j in gray_mat.D[1]: # iterate over columns labels
        for i in gray_mat.D[0]: # iterate over rows
            gray_mat[i,j] = gray_dict[j] # (i,j) entry gets look up value corresponding to column label
    return gray_mat


# Task 4.15.11: Write a procedure reflect_about(x1,y1,x2,y2) that takes two points and returns a matrix that reflects
# about the line defined by the two points

def reflect_about(x1,y1,x2,y2):
    """
    This procedure returns a transformation matrix that reflects about the line
    passing through (x1,y1), (x2,y2).

    :param x1: x coordinate of point 1
    :param y1: y coordinate of point 1
    :param x2: x coordinate of point 2
    :param y2: y coordinate of point 2
    """
    # this procedure uses rotations, and reflections to reflect over the line through the given points

    m = (y2-y1)/(x2-x1) # calculate slope of line L through given points
    theta_L = math.atan(m) # calculate angle between line L and x-axis by using the slope of L
    rotate_to_x = rotation(-theta_L) # create rotation matrix that rotates line L to the x-axis
    ref_im = reflect_x() # reflect over image of line L, which is the x-axis
    rotate_back = rotation(theta_L) # rotate back to original line
    return rotate_back*ref_im*rotate_to_x # composite transformation is product of the three matrices (in this order)




# Alternative method of reflecting over line. Much messier but uses the idea of constructing the matrix of a linear 
# transformation by using the images of (1,0) and (0,1) as the columns of the transformation matrix.
# the matrix ref_L_mat below reflects over line L passing through (0,0) and (a,b). col 1 of ref_L_mat is image of (1,0)
# when reflected over L. column 2 is image of (0,1) when reflected over L. The reflection is equivalent to a rotation of
# twice the angle from the point in question to L

# 1. translate original points so that one point is at the origin
# 2. use ref_L_mat to reflect over L
# 3. translate image of previous step back (invert step 1)

# The define translation procedure above uses a 3x3 matrix homogenous coordinates whereas the matrix below is 2x2.
# However, I am noting the existence of the matrix

# the procedure below returns a rotation matrix that reflects about a line passing through (a,b) and the origin.

def reflect_about_L(x1,y1,x2,y2):
    """
    This procedure returns a transformation matrix that reflects about the line
    passing through (0,0) and (a,b) using a single matrix.
    This is in contrast to reflect_about() which uses composite transformations. In particular
    this procedure uses the idea of constructing the matrix of a linear transformation by
    using the images of (1,0) and (0,1) as the columns of the transformation matrix. In this instance
    reflection is performed by using rotation by twice the angle of theta (and some trig identities),
    where theta is the angle between the line and the x-axis.

    :param x1: x coordinate of point 1
    :param y1: y coordinate of point 1
    :param x2: x coordinate of point 2
    :param y2: y coordinate of point 2
    """

    m = (y2 - y1) / (x2 - x1)  # calculate slope of line L through given points
    theta_L = math.atan(m)  # calculate angle between line L and x-axis by using the slope of L
    ref_L_mat = Mat(({0,1},{0,1}), #matrix that reflects over L by using rotations
                {(0,0):math.cos(2*theta_L),(1,0):math.sin(2*theta_L),
                 (0,1):math.sin(2*theta_L),(1,1):-math.cos(2*theta_L)})
    return ref_L_mat
   


