import models.material_point
import managers.v1_x
import managers.v2_y
import numpy
import models.space_point
import models.space_grid
def move_through_space(time, h, grid_axis):
    t = h
    m = 0
    grid_length = grid_axis * 2 + 1
    a = numpy.linspace(-grid_axis, grid_axis, grid_length)
    x_s, y_s = numpy.meshgrid(a, a)
    velocity_fields = []
    for n in range(int(time / h) + 1):
        space_points = []
        for i in range(grid_length):
            for j in range(grid_length):
                x = x_s[i, j]
                y = y_s[i, j]
                space_points.append(models.space_point.SpacePoint(m, x, y, managers.v1_x.v1_x(t, x), managers.v2_y.v2_y(t, y), t))
                m += 1
            velocity_fields.append(models.space_grid.SpaceGrid(space_points))
        t += h
        return velocity_fields
