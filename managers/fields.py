import matplotlib.pyplot as plt
import numpy
import math
def plot_velocity_fields(velocity_fields, grid_axis,h):
    t = h
    grid_length = grid_axis * 2 + 1
    for n in range(len(velocity_fields)):
        plt.figure(n)
        plt.suptitle('t = ' + str(t))
        m = 0
        coord_x = []
        coord_y = []
        v_x = []
        v_y = []
        for i in range(grid_length):
            for j in range(grid_length):
                coord_x.append(velocity_fields[n].space_points[m].coord_x)
                coord_y.append(velocity_fields[n].space_points[m].coord_y)
                v_x.append(velocity_fields[n].space_points[m].velocity_x)
                v_y.append(velocity_fields[n].space_points[m].velocity_y)
                m += 1
        plt.subplot(1, 2, 1)
        plt.quiver(coord_x, coord_y, v_x, v_y)

        Y, X = numpy.mgrid[-10:10:0.02,
                     -10:10:0.02]
        U = - math.exp(t) * X
        V = t * Y
        C = numpy.sqrt((V**2)+U**2)
        plt.subplot(1, 2, 2)
        plt.axis([-grid_axis, grid_axis, -grid_axis, grid_axis])
        plt.streamplot(X, Y, U, V,
                       density = 4,
                       arrowsize = 1+0.2,
                       linewidth =  1,
                       color = C,
                       cmap ='winter')
        t += h
        plt.show()