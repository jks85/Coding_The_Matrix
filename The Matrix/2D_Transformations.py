# Lab 4.15: Transformations in 2D Geometry
# Linear Algebra Coding the Matrix, Ed. 1


from mat import Mat
from vec import Vec
import image_mat_util


# images will be represented as matrices containing coordinates
# points will be represented via location and color with a vector for each attribute
# location vec labels/domain: {'x','y','u'}
# color vec labels/domain: {'r','g','b}
# Note: u = 1 in location vector to allow certain transformations

# point at (12,15) has vector Vec({'x','y','u'},{'x':12, 'y':15, 'u':1})
# color red represented by  Vec({'r','g','b},{'r':1})

# pixel grids are quadrilaterals not necessarily rectangles
# coordinates of top left 4 corners: (0,0), (1,0) (0,1), (1,1)

# location matrix: row labels {'x','y','u'}, col labels {(0,0), (1,0) (0,1), (1,1) ...}
# color matrix: row labels {'r','g','b}, col labels {(0,0), (1,0) (0,1), (1,1) ...}

# Task 4.15.1
# Use image_mat_util module to load a png file and display it on screen

img_mat = image_mat_util.file2mat('C:\\Users\\jksim\\PycharmProjects\\Coding The Matrix\\The Matrix\\img01.png')
image_mat_util.mat2display(img_mat[0],img_mat[1])

# See transform.py for remaining 4.15 tasks

