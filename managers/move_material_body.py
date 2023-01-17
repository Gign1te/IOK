import models.material_point
import managers.v1_x
import managers.v2_y
import models.point_trajectory
import models.body_trajectory


def move_material_body(time, h, mb):
    point_trajectories = []
    c1 = 0
    c2 = 1 / 2
    c3 = 1 / 2
    c4 = 1
    a11 = 0
    a21 = 1 / 2
    a22 = 0
    a31 = 0
    a32 = 1 / 2
    a33 = 0
    a41 = 0
    a42 = 0
    a43 = 1
    a44 = 0
    b1 = 1 / 6
    b2 = 2 / 6
    b3 = 2 / 6
    b4 = 1 / 6
    for i in range(len(mb.material_points)):
        t = 1
        x_0 = mb.material_points[i].x_0
        y_0 = mb.material_points[i].y_0
        x_t = [x_0]
        y_t = [y_0]
        for n in range(int(time / h) + 1):
            x_k = x_t[n]
            y_k = y_t[n]
            f_1x = managers.v1_x.v1_x(t, x_k)
            f_2x = managers.v1_x.v1_x(t + c2 * h, x_k + h * a21 * f_1x)
            f_3x = managers.v1_x.v1_x(t + c3 * h, x_k + h * a31 * f_1x + h * a32 * f_2x)
            f_4x = managers.v1_x.v1_x(t + c4 * h, x_k + h * a41 * f_1x + h * a42 * f_2x + h * a43 * f_3x)
            f_1y = managers.v2_y.v2_y(t, y_k)
            f_2y = managers.v2_y.v2_y(t + c2 * h, y_k + h * a21 * f_1y)
            f_3y = managers.v2_y.v2_y(t + c3 * h, y_k + h * a31 * f_1y + h * a32 * f_2y)
            f_4y = managers.v2_y.v2_y(t + c4 * h, y_k + h * a41 * f_1y + h * a42 * f_2y + h * a43 * f_3y)
            x_t.append(x_k + h * (b1 * f_1x + b2 * f_2x + b3 * f_3x + b4 * f_4x))
            y_t.append(y_k + h * (b1 * f_1y + b2 * f_2y + b3 * f_3y + b4 * f_4y))
            t += h
        point_trajectories.append(models.point_trajectory.PointTrajectory(mb.material_points[i], x_t, y_t))
    body_trajectory = models.body_trajectory.BodyTrajectory(point_trajectories, mb)
    return body_trajectory